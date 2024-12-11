import os
import pandas as pd
import numpy as np
import tensorflow as tf
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# App initialization
app = FastAPI(title="Recipe Recommendation API")

# Load dataset
DATASET_PATH = 'dataset/Final_Dataset1.csv'
data = pd.read_csv(DATASET_PATH)

# Prepare data processing components
data['text'] = data['Title'] + ' ' + data['Ingredients'] + ' ' + data['Steps']

# Load pre-trained model
MODEL_PATH = 'model/Recipe_Recomendation_Model_v2.h5'
model = tf.keras.models.load_model(MODEL_PATH)

# Recreate tokenizer and label encoder
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=5000)
tokenizer.fit_on_texts(data['text'])

label_encoder = tf.keras.preprocessing.text.Tokenizer()
label_encoder.fit_on_texts(data['Category'])

# Calculate max length for padding (should match training)
max_length = max(len(x.split()) for x in data['text'])

# Input model for API
class RecipeRequest(BaseModel):
    CategoryUser: str
    TempUser: int
    TimeUser: int

# Recommendation function
def recommend_recipe(CategoryUser, TempUser, TimeUser):
    # Proses Temp
    temp_condition = 1 if TempUser <= 27 else 0

    # Proses Waktu
    if 6 <= TimeUser < 10:
        type_condition = "Makan Pagi"
    elif 11 <= TimeUser < 14:
        type_condition = "Makan Siang"
    elif 18 <= TimeUser < 21:
        type_condition = "Makan Malam"
    else:
        type_condition = None  # Semua tipe makanan diperbolehkan

    # Filter dataset berdasarkan input pengguna
    filtered_data = data[(data['Category'] == CategoryUser) & (data['Temp(cold)'] == temp_condition)]

    if type_condition:
        filtered_data = filtered_data[filtered_data['Type'].str.contains(type_condition)]

    # Prepare prediction scores
    def get_prediction_score(text):
        seq = tokenizer.texts_to_sequences([text])
        padded_seq = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=max_length, padding='post')
        return model.predict(padded_seq).max()

    # Menghitung skor kemiripan
    filtered_data['score'] = filtered_data['text'].apply(get_prediction_score)

    # Mengambil Id, Title, dan score kemiripan
    recommendations = filtered_data[['Id', 'Title', 'Type', 'Temp(cold)', 'score']].sort_values(by='score', ascending=False)

    return recommendations.head(12).to_dict(orient='records')

# API Endpoint
@app.post("/recommend")
async def get_recommendations(request: RecipeRequest):
    try:
        recommendations = recommend_recipe(
            request.CategoryUser, 
            request.TempUser, 
            request.TimeUser
        )
        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Recipe Recommendation API"}
