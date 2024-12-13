# Machine Learning Path
## C242-PS547
### Team Members

| Status   | Path | Name                         | Bangkit ID     | University                    | LinkedIn                                                                        | GitHub                                        |
| -------- | ---- | ---------------------------- | -------------- | ----------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------- |
| `Active` | (CC) | Nurminati Hasnatul Khatimah  | `C247B4KX2427` | Universitas Lambung Mangkurat | [LinkedIn](https://www.linkedin.com/in/nurminati-hasnatul-khatimah-704b69244/)  | [GitHub](https://github.com/minacloe)         |
| `Active` | (CC) | Muhammad Adji Maulana Putera | `C247B4KY2686` | Universitas Lambung Mangkurat | [LinkedIn](https://www.linkedin.com/in/muhammad-adji-maulana-putera-514066252/) | [GitHub](https://github.com/adjimaulanap)     |
| `Active` | (ML) | Balladiva Mahesi             | `M008B4KX0804` | Universitas Gadjah Mada       | [LinkedIn](https://www.linkedin.com/in/balladiva-mahesi-428a16256/)             | [GitHub](https://github.com/bldv)             |
| `Active` | (ML) | Alif Rahmatullah Lesmana     | `M668B4KY0386` | STMIK Palangka Raya           | [LinkedIn](https://www.linkedin.com/in/alif-rahmatullah-lesmana-565028311/)     | [GitHub](https://github.com/Peparrepair)      |
| `Active` | (ML) | Muhammad Raffa Saputra       | `M668B4KY2987` | STMIK Palangka Raya           | [LinkedIn](https://www.linkedin.com/in/muhammad-raffa-saputra21/)               | [GitHub](https://github.com/21YeetYa)         |
| `Active` | (MD) | Riyan Fazri Rahman           | `A668B4KY3894` | STMIK Palangka Raya           | [LinkedIn](https://www.linkedin.com/in/riyan-fazri-rahman/)                     | [GitHub](https://github.com/riyanfazrirahman) |

---
## Overview
We built a Machine Learning model for Temfore application using TensorFlow as the framework, and then utilized VSCode and Google Colab as the IDEs. In the process, we used pandas for data manipulation, followed by Numpy and scikit-learn for score calculations and recommendation functions.
## Data Wrangling
In Data Wrangling, the application manipulates and cleans the Indonesian recipes dataset by performing several key tasks: reading and cleaning the CSV file by removing missing values and duplicates, adding a category column based on the file name, merging the cleaned data into a single file with an 'Id' column, and further cleaning the text in certain columns. In addition, it also added new columns, grouped the data by category, retrieved and downloaded recipe images from URLs, and replaced problematic characters in the data set. Finally, the cleaned data set was converted from CSV to JSON format for easy database uploading, and the results were saved in a JSON file.
## Model
The model uses a sequential architecture with an embedding layer for word representation and a bidirectional GRU layer to capture sequential context. The accuracy achieved after performing the evaluation was around 0.9570 or 0.96, showing strong performance on the classification task. After training, the model was exported in .h5 format. In addition, FastAPI was used to create an API to attempt processing.
![alt text](accuracy.png)
