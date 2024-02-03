import json

def concat_meanings(input_file, output_file):
    # Load the JSON data from the file
    with open(input_file, 'r', encoding='utf-8') as f:
        kanji_data = json.load(f)

    # Concatenate the meanings for each kanji into one string, separated by ", "
    for entry in kanji_data:
        entry['caption'] = ', '.join(entry['meanings'])

    # Save the modified data to a new JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(kanji_data, f, ensure_ascii=False, indent=4)


# Example usage:
# Replace 'path_to_your_input.json' with the path to your JSON file
# and 'path_to_your_output.json' with the path where you want to save the output JSON.
concat_meanings('kanji_data.json', 'combined_kanji.json')
