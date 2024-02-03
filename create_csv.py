import json
import csv

def json_to_csv(json_input_path, csv_output_path):
    # Read the JSON data from the file
    with open(json_input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Open the CSV file for writing
    with open(csv_output_path, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        csvwriter = csv.writer(csvfile)
        
        # Write the header
        csvwriter.writerow(['file_name', 'caption'])
        
        # Write the data rows
        for entry in data:
            csvwriter.writerow([entry['file_name'], entry['caption']])

# Replace 'path/to/your/input_file.json' with the path to your JSON file
# Replace 'path/to/your/output_file.csv' with the path where you want to save the CSV
json_input_path = 'complete_kanji_data.json'
csv_output_path = 'metadata.csv'

# Call the function to convert and save the data as CSV
json_to_csv(json_input_path, csv_output_path)
