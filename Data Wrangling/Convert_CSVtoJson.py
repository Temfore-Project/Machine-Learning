import csv
import json

dataNew = 'Final_Dataset1.csv'

OutputAfter = "Final_Dataset1.json"

with open(dataNew, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile, delimiter=',')

    json_data = []
    
    for row in reader:
        print(f"Header: {reader.fieldnames}")
        print(f"Row Data: {row}")

        record = {
            "Id": row.get("Id", "").strip(),
            "Category": row.get("Category", "").strip(),
            "Title": row.get("Title", "").strip(),
            "Ingredients": row.get("Ingredients", "").strip(),
            "Steps": row.get("Steps", "").strip(),
            "URL": row.get("URL", "").strip(),
            "Type": row.get("Type", "").strip(),
            "Temp(cold)": row.get("Temp(cold)", "").strip()
        }
        
        print(f"Record processed: {record}")
        
        if any(record.values()):
            json_data.append(record)
        else:
            print("This line is empty and not entered:", record)

    with open(OutputAfter, mode='w', encoding='utf-8') as outfile:
        json.dump(json_data, outfile, indent=4, ensure_ascii=False)

print(f"The file has been successfully processed and saved as '{OutputAfter}'")
