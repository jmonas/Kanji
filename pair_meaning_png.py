import json

def concat_meanings(input_file, dictionary , output_file):
    # Load the JSON data from the file
    with open(input_file, 'r', encoding='utf-8') as f:
        kanji_data = json.load(f)
    with open(dictionary, 'r', encoding='utf-8') as k:
        dictionary_data = json.load(k)
    
    
    # Concatenate the meanings for each kanji into one string, separated by ", "
    i =0
    for entry in kanji_data:
        i+=1
        # print(i)
        try:
            id = dictionary_data[entry["literal"]][-1][:-4]
            entry['file_name'] = f"kanji_{id}.png"
            entry['caption'] = ', '.join(entry['meanings'])
        except:
            i-=1
            entry["literal"]
            del entry
    print(i)


    # Save the modified data to a new JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(kanji_data, f, ensure_ascii=False, indent=4)


# Example usage:
# Replace 'path_to_your_input.json' with the path to your JSON file
# and 'path_to_your_output.json' with the path where you want to save the output JSON.
concat_meanings('combined_kanji.json', 'kvg-index.json' ,'complete_kanji_data.json')
