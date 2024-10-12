import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        line = line.lower().translate(str.maketrans('', '', string.punctuation))
                        words.extend(line.split())
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f'Файл {file_name} не найден.')
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word) + 1
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for name, words in all_words.items():
            result[name] = words.count(word)
        return result


# if __name__ == '__main__':

finder = WordsFinder('test_file.txt')
finder2 = WordsFinder('test_file2.txt')
finder3 = WordsFinder('test_file3.txt')

print(finder.get_all_words())
print(finder2.get_all_words())
print(finder3.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))