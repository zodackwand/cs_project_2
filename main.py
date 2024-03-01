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
    
    def word_ladder(start, end, word_list = [word.strip() for word in open('words_alpha.txt', 'r')]):
        queue = [(start, [start])]
        visited = set()

        while queue:
            current_word, current_path = queue.pop(0)

            if current_word == end:
                return current_path

            visited.add(current_word)
            neighbors = find_neighbors(current_word, word_list)

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, current_path + [neighbor]))

        return None  # No word ladder found
        
        