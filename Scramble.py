import random
import itertools

class Scramble:
    def __init__(self):
        self._points = 0
        self._solution = []
        self._letters = []
        self._answer = []
        self._score = 0

    def generate(self):

        # read all 5 letter words from textfile and randomly selects one
        f = open("fiveletterwords.txt", 'r')
        list_of_words = f.read().splitlines()
        f.close()

        word = list_of_words[random.randint(0,len(list_of_words))]

        letters = list(word)  # separate word into array of characters

        # scramble letters
        for i in range(len(letters)):
            randomPosition = random.randint(0,4)
            temp = letters[i]
            letters[i] = letters[randomPosition]
            letters[randomPosition] = temp

        self._letters = letters

    def update_points(self, answer):
        points = 0
        letters = list(answer)

        if not self.is_word(answer):
            points -= 2
        else:
            for i, c in enumerate(letters):
                if c in ['a', 'e', 'o', 't', 'i', 'n', 'r', 's', 'l', 'u']:
                    points += 1
                elif c in ['d', 'g']:
                    points += 2
                elif c in ['c', 'm', 'b', 'p',]:
                    points += 3
                elif c in ['h', 'f', 'w', 'y', 'v']:
                    points += 4
                elif c in ['k']:
                    points += 5
                elif c in ['j', 'x']:
                    points += 8
                elif c in ['q', 'z']:
                    points += 10
        return points

    def get_points(self):
        return self._points

    def set_points(self, points):
        self._points = points

    def create_solution(self):
        word = "water"
        combinations = []
        solution = []

        # creates all combinations of letters in an array
        for i in range(len(word)+1):
            for combination in itertools.combinations(word, i):
                combinations.append(''.join(combination))

        combinations.pop(0) # gets rid of the first index, which holds nothing

        # goes through each combination and finds all permutations
        for i in range(len(combinations)):
            for j in itertools.permutations(combinations[i]):
                # checks if permutation makes a real word and stores it in an array if it does
                if self.is_word(j):
                    solution.append(''.join(j))

        return solution

    def evaluate_score(self):
        maxPoints = 0
        solution = self.create_solution()
        for i in range(len(solution)):
            maxPoints += self.update_points(solution[i])

        return self._points / maxPoints * 100

    def is_word(word):
        return True

    def store_answer(self, answer):
        answerLetters = list(answer)
        validLetters = self._letters
        check = False

        for i in range(len(answerLetters)):
            if answer[i] in validLetters:
                validLetters.pop(validLetters.index(answer[i]))
                check = True
            else:
                check = False
                break

            if check:
                self._answer.append(answer)

