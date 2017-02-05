import tkinter
import time
from Scramble import *

# if __name__ == '__main__':
#     root = tkinter.Tk()
#     root.mainloop()

game = Scramble()

# generate game
game.generate()
print(game.get_letters())

# user puts in words
user_input = input('Please enter a word: ')

if game.store_answer(user_input):
    pt = game.update_points(user_input)
    game.set_points(pt)
    print('Points: {0}'.format(game.get_points()))
else:
    print('Invalid Input')