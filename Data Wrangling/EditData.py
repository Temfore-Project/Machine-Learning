import pandas as pd
import os

#Here the process of labeling data is almost complete

data = "ayam"

#Use this code for new files
dataNew = f"Data Wrangling/Data_Complete/{data}_data_complete.csv"

#Use this code to load files that have previously been edited but not finished
# dataNew = f"Data Wrangling/Data_Complete/data_complete/{data}_data_complete_done.csv"

OutputFolder = f"Data Wrangling/Data_Complete/data_complete"
 
if not os.path.exists(OutputFolder):
    os.makedirs(OutputFolder)

df = pd.read_csv(dataNew)

#Change checkpoints to continue previous progress
checkpoint = 0

for index, row in df.iterrows():
    if index < checkpoint:
        continue
    print(f"\nCheckpoint : {index}")
    print(f"Row : {index+1}")
    print(f"Id : {row['Id']}")
    print(f'Title : {row['Title']}')
    print(f'\nType : {row['Type']}')
    print(f'Temp(cold) : {row['Temp(cold)']}')
    dtEdit = input("\nEdit data? Input 'n' to go to the next data, and 'y' to save the current data and exit : ")
    if dtEdit == "n":
        print("Go to the next data")
        continue
    elif dtEdit == "y":
        break
    
    print(f'\n{row['Ingredients']}')
    ingre_ = str(input("\nEnter new Ingredients data (input 'n' if you don't want to change) : "))

    print(f"\n{row['Steps']}")
    stps_ = str(input("\nEnter new Steps data (input 'n' if you don't want to change) : "))

    answer1 = int(input("\nMakan Pagi? 1=True : "))
    answer2 = int(input("Makan Siang? 1=True : "))
    answer3 = int(input("Makan Malam? 1=True : "))
    answer4 = int(input("Hidangan Utama? 1=True : "))
    answer5 = int(input("Lauk Pauk? 1=True : "))
    answer6 = int(input("Sup? 1=True : "))
    answer7 = int(input("Sayur? 1=True : "))
    answer8 = int(input("Cemilan? 1=True : "))
    answer9 = int(input("\nTemp(Dingin)? 1=True : "))

    #Update the values in the Ingredients and Steps columns if there are any changes.
    if ingre_ == "n":
        pass
    else:
        df.at[index, 'Ingredients'] = ingre_

    if stps_ == "n" :
        pass
    else:
        df.at[index, 'Steps'] = stps_

    jenis1 = "Makan Pagi--" if answer1 == 1 else ""
    jenis2 = "Makan Siang--" if answer2 == 1 else ""
    jenis3 = "Makan Malam--" if answer3 == 1 else ""
    jenis4 = "Hidangan Utama--" if answer4 == 1 else ""
    jenis5 = "Lauk Pauk--" if answer5 == 1 else ""
    jenis6 = "Sup--" if answer6 == 1 else ""
    jenis7 = "Sayur--" if answer7 == 1 else ""
    jenis8 = "Cemilan--" if answer8 == 1 else ""
    temp = int(1) if answer9 == 1 else 0
    
    #Combine all food types into 1 variable
    update_value = f'{jenis1}{jenis2}{jenis3}{jenis4}{jenis5}{jenis6}{jenis7}{jenis8}'
    
    #Update values in Type and Temp columns
    df.at[index, 'Type'] = update_value
    df.at[index, 'Temp(cold)'] = temp

    print(f"The data is updated with the following data :")
    print(f'Title : {df.at[index, 'Title']}')
    print(f'Ingrdients : ')
    print(f"{df.at[index, 'Ingredients']}")
    print(f'Steps : ')
    print({df.at[index, 'Steps']})
    print(f'Type : {update_value}')
    print(f'Temp : {temp}')

output_file = os.path.join(OutputFolder, f"{data}_data_complete_done.csv")
df.to_csv(output_file, index=False)
print(f"\nThe updated data is saved to the file: {output_file}")
