import os

# Folder containing the OCR'd text files
input_folder = r"F:\Projects folder\RAG-LLM\Pre-processed data"
output_file = r"F:\Projects folder\RAG-LLM\merged_bengali_text.txt"

# Get all .txt files sorted by filename (page_1, page_2, ..., page_47)
txt_files = sorted(
    [f for f in os.listdir(input_folder) if f.endswith(".txt")],
    key=lambda x: int(''.join(filter(str.isdigit, x)))
)

# Merge them
with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in txt_files:
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as infile:
            outfile.write(infile.read())
            outfile.write("\n\n")  # Add spacing between pages

print(f"✅ All files merged into:\n{output_file}")
