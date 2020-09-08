
class ManipulateString:
    def only_alnums(self, string):
        #split by sentences and words
        paragraph = string.split("\n")[:-1]
        s = set()
        for sentence in paragraph:
            for word in sentence.split():
                w = ""
                for letter in word:
                    if letter.isalnum():
                        w += letter
                s.add(w)

        return s

    def get_text(self):
        text = input("Input your sentence / paragraph here (type exit to end): \n")
        whole_text = ""
        while text != "exit":
            whole_text += text + "\n"
            text = input()
        # clean the sentences
        whole_text = self.only_alnums(whole_text)
        return whole_text


class WordFile(ManipulateString):
    def __init__(self):
        super().__init__()
        self.file_name = "words.txt"
        self.length_row = 60

    def text_to_file(self, list_of_words):
        s = ""
        count_w = 0
        for ind_word in range(len(list_of_words)):
            w = list_of_words[ind_word].lower() + " "
            count_w += len(w)
            if count_w > self.length_row:
                count_w -= self.length_row
                s += w[:count_w] + "\n" + w[count_w:]
            else:
                s += w
        return s
    def write_new(self):
        list_words = list(self.get_text())
        s = self.text_to_file(list_words)
        with open(self.file_name, "w") as f:
            f.write(s)
        return "Changed Successfully"

    def add_words(self):
        new_words = self.get_text() # return set of elements/words
        existing_words = self.read_content().split()
        unique_new_words = []

        for new_word in new_words:
            new_word = new_word.lower()
            if new_word not in existing_words:
                unique_new_words.append(new_word)
        s = self.text_to_file(unique_new_words)
        with open(self.file_name, "a") as f:
            f.write(s)
        return "Added Successfully"

    def read_content(self):
        with open(self.file_name, "r") as f:
            return f.read()


if __name__ == "__main__":
    w = WordFile()
    wordfile_methods = [w.write_new, w.read_content, w.add_words]
    while True:
        try:
            choice = int(input("Choice: \n"))
            print(wordfile_methods[choice]())
        except IndexError as i:
            print(i)
        except ValueError as v:
            print(v)