import time

class Game:
    def find_neighbours(self):
        pass

    def word_ladder(self):
        pass

def main():
    # Initialize the class and ask input
    game = Game()
    start_word = input()
    end_word = input()

    # Get the path
    start_time = time.time()
    path_array = game.word_ladder(start_word, end_word)
    end_time = time.time()

    execution_time = end_time - start_time

    # Print the results
    for i in path_array:
        print(i, end='')

    # Print execution time
    print(execution_time)