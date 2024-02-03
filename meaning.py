import xml.etree.ElementTree as ET
import json

# The path to your kanjidic2 XML file
kanjidic2_file_path = 'kanjidic2.xml'

# Parse the XML file directly
tree = ET.parse(kanjidic2_file_path)
root = tree.getroot()

# Create a list to hold all kanji entries
kanji_list = []

# Iterate through each character in the file
for character in root.findall('character'):
    kanji_dict = {}
    kanji_dict['literal'] = character.find('literal').text
    kanji_dict['meanings'] = [m.text for m in character.findall('reading_meaning/rmgroup/meaning') if 'm_lang' not in m.attrib]
    
    kanji_list.append(kanji_dict)

# Now write the kanji list to a JSON file
with open('kanji_data.json', 'w', encoding='utf-8') as f:
    json.dump(kanji_list, f, ensure_ascii=False, indent=4)

# Output to verify that the file was created
print("Kanji data has been written to kanji_data.json")
