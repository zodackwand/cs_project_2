#creating a list of the words from words_alpha.txt
f = open('words_alpha.txt')
words_list = []
for word in f.read().split():
    words_list.append(word)
class Game:

    def find_neighbours(self, target_word, lst):
        neighbours = []
        words = []
        count = 0
        target_letters = [*target_word]
        for w in lst:
            if len(w) == len(target_word):
                words.append(w)
        for w in words:
            letters = [*w]
            for i in range(len(w)):
                if letters[i] == target_letters[i]:
                    count += 1
            if count == (len(target_word) - 1):
                neighbours.append(w)
            count = 0
        return neighbours

    def input_start_word(self, start_word):
        return start_word

    def input_end_word(self, end_word):
        return end_word
