class Game:
    def find_neighbours(self):
        pass
    
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
        
        