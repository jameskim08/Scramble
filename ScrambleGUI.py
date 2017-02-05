import tkinter as tk
from tkinter import messagebox
from Scramble import *

class ScrambleGUI:
    def __init__(self, master):
        master.minsize(width=1000, height=600)
        master.maxsize(width=1000, height=600)
        self.master = master
        self.mainframe = tk.Frame(self.master, bg='#FFFFFB')
        self.mainframe.pack(fill=tk.BOTH, expand=True)

        self.scramble = Scramble()
        self.scramble.generate()

        self.display_points = tk.StringVar()
        self.display_points.trace('w', self.build_points)

        self.answer = tk.StringVar()
        self.answer.trace('w', self.build_answer_box())

        self.build_grid()
        self.build_letters()
        self.build_answer_box()
        self.build_user_input()
        # self.build_new_game_button()
        # self.build_timer()
        self.build_points()



    def build_grid(self):
        self.mainframe.columnconfigure(0,weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=1)
        self.mainframe.rowconfigure(3, weight=1)
        self.mainframe.rowconfigure(4, weight=1)

        self.labelframe = tk.Frame(self.mainframe, bg="#FFFFFB")
        self.labelframe.grid(row=1, column=0)
        self.labelframe.columnconfigure(0, weight=0)
        self.labelframe.columnconfigure(1, weight=0)

    def build_letters(self):
        letters_frame = tk.Frame(self.mainframe, bg='#FFFFFB')
        letters_frame.grid(row = 0, column=0)
        letters_frame.columnconfigure(0, weight=1)
        letters_frame.columnconfigure(1, weight=1)
        letters_frame.columnconfigure(2, weight=1)
        letters_frame.columnconfigure(3, weight=1)
        letters_frame.columnconfigure(4, weight=1)

        self.letters = []

        for i in range(5):
            self.letters.append(tk.Label(
                letters_frame,
                text= self.scramble.get_letters(i).upper(),
                fg='#5B5F97',
                bg='#FFFFFB',
                font=('Helvetica', 50)
            ))
            self.letters[i].grid(row=0, column=i, sticky='nsew', padx=50, pady=10)

    def build_user_input(self):
        self.user_input = tk.Entry(
            self.mainframe,
            width='30',
            font=('Helvetica', 18),
            bd='1.5',
            justify='center'
        )
        self.user_input.grid(row=2, column=0)
        self.user_input.bind('<Return>', self.input_entered)


    def input_entered(self, event):
        user_guess = str(self.user_input.get())
        print(user_guess)

        if self.scramble.check_answer(user_guess):
            self.scramble.set_answers(user_guess)
            points = self.scramble.calculate_points(user_guess)
            self.scramble.set_points(points)
            self.display_points.set(self.scramble.get_points())
            self.answer.set(self.scramble.get_answer[-1])
            # TODO: print to answer box
            # TODO: update points label
        else:
            print("invalid answer")
            # TODO: print to error box
        self.user_input.select_clear()

    def build_points(self, *args):
        display_points = tk.Label(
            self.labelframe,
            text="Points: {0}".format(self.display_points.get()),
            fg ='#5B5F97',
            bg='#FFFFFB',
            font=('Helvetica', 18)
        )
        display_points.grid(row=0, column=0, sticky ='nswe', padx=10, pady=5)

    def build_answer_box(self, *args):
        answer_box = tk.Listbox(
            self.mainframe,

        )
        answer_box.insert(self.answer.get())

        answer_box.grid(row=4, column=0)



