import os

file1 = "math_notes.txt"
file2 = "science_notes.txt"
merged_file = "all_study_notes.txt"

with open(file1, "w") as f1:
    f1.write("Math covers algebra and geometry basics.")

with open(file2, "w") as f2:
    f2.write("Science covers physics and chemistry concepts.")

# 2. Check and remove old merged file if it exists
if os.path.exists(merged_file):
    os.remove(merged_file)
    print("Old merged file removed.")

# 3. Read files safely and count words
files_to_merge = [file1, file2]
total_words = 0

with open(merged_file, "w") as outfile:
    for fname in files_to_merge:
        if os.path.exists(fname):
            with open(fname, "r") as infile:
                content = infile.read()
                word_count = len(content.split())
                total_words += word_count
                
                # Write to the merged file
                outfile.write(f"--- Content from {fname} ---\n")
                outfile.write(content + "\n\n")
                print(f"File {fname} has {word_count} words.")

print(f"Merge complete. Total words in combined file: {total_words}")