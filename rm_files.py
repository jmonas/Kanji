import os
import csv

# Path to your CSV file
csv_file_path = 'metadata.csv'

# Path to the directory containing the files you want to check against the CSV
directory_path = 'pngs'

# Read all filenames listed in the CSV into a set for faster lookup
files_in_csv = set()
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Assuming the column containing the file names in the CSV is named 'file_name'
        files_in_csv.add(row['file_name'])

# Check each file in the directory against the set of filenames from the CSV
for filename in os.listdir(directory_path):
    if filename not in files_in_csv:
        file_path = os.path.join(directory_path, filename)
        # Uncomment the next line to actually delete the files
        os.remove(file_path)
        print(f"Deleted {file_path}")

# Be cautious and verify the file names and paths before uncommenting the os.remove line.
