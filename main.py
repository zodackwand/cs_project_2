import time

#creating a list of the words from words_alpha.txt
f = open('words_alpha.txt')
words_list = []
for word in f.read().split():
    words_list.append(word)
    
class Game:
    def find_neighbors(self, target_word, lst):
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
    
    def word_ladder(self, start, end, words_list):
        queue = [(start, [start])]
        visited = set()

        while queue:
            current_word, current_path = queue.pop(0)

            if current_word == end:
                return current_path

            visited.add(current_word)
            neighbors = self.find_neighbors(current_word, words_list)

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, current_path + [neighbor]))

        return None  # No word ladder found

def main():
    # Initialize the class and ask input
    game = Game()
    start_word = input('Enter start word: ')
    end_word = input('Enter end word: ')

    # Get the path
    start_time = time.time()
    path_array = game.word_ladder(start_word, end_word, words_list)
    end_time = time.time()

    execution_time = end_time - start_time

    # Print the results
    if path_array is not None:
        for word in path_array:
            print(word, end=' ')
    else:
        print("No word ladder found.")

    # Print execution time
    print(f'Execution time: {execution_time}')
        
if __name__ == "__main__":
    main()