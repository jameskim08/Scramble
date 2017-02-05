import random
import itertools
import requests

class Scramble:


    def __init__(self):
        """ Initializes the game class

        Attributes:
            _points: User's points
            _solution: All the possible word user can make
            _letters: Given letters users can work with
            _answers: List of correct words
            _score: users's score
        """
        self._points = 0
        self._solution = []
        self._letters = []
        self._answer = []
        self._score = 0

    def generate(self):
        """ Function that generates the game  """

        # read all 5 letter words from textfile and randomly selects one
        f = open("fiveletterwords.txt", 'r')
        list_of_words = f.read().splitlines()
        f.close()

        # Randomly selects a word
        word = list_of_words[random.randint(0, len(list_of_words))]

        letters = list(word)  # separate word into array of characters

        # scramble letters
        for i in range(len(letters)):
            randomPosition = random.randint(0,4)
            temp = letters[i]
            letters[i] = letters[randomPosition]
            letters[randomPosition] = temp

        self._letters = letters    # save the possible letters into the attributes

    def update_points(self, answer):
        """ Function that checks if user enters a valid word"""
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

    def get_letters(self):
        return self._letters

    def get_points(self):
        return self._points

    def set_points(self, points):
        self._points = points

    def create_solution(self):
        """ Generates all possible words and puts it in an array"""
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
        """ Called when gamee is done to tell user the score"""
        maxPoints = 0
        solution = self.create_solution()
        for i in range(len(solution)):
            maxPoints += self.update_points(solution[i])

        return self._points / maxPoints * 100

    def is_word(self, answer):
        """ API call to dictionaey to see if word exists"""
        if not isinstance(answer, str):
            print('{} is not type a string')
            return False

        dict_api_url = 'https://wordsapiv1.p.mashape.com/words/' + str(answer)

        headers = {
            "X-Mashape-Key": "hgcPlTTMlRmshD1vW3RDL8QfM1Dsp1tkFhRjsnbwU0Vjq9xR9I",
            "Accept": "application/json"
        }
        req = requests.get(dict_api_url, headers=headers)

        if req.status_code == 200:
            return True
        else:
            return False

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
        return check
