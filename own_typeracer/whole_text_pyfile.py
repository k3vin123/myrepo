file_name = "all_text_files\\text1.txt"

with open(file_name, 'r') as f:
    words = f.read().split("\n")

if __name__ == "__main__":
    print(words)