from datasets import load_dataset

dataset = load_dataset("imagefolder", data_dir="/Users/owner/Desktop/sakana/3/pngs")
print(dataset.column_names)
dataset.push_to_hub("jmonas/kanji")