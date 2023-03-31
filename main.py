# By: Noah Schlaupitz
# Calculator App
import os
import tkinter as tk
from collections import namedtuple
from PIL import Image
import imagehash as ih
import hashlib
from os import listdir

# --- Constants ---
# notes
# add specific error funtionality
# truncate expression


# Fonts
EXP_FONT = ("Comic Sans", 48, "bold")
TTL_FONT = ("Comic Sans", 16)
DIGITS_FONT = ("Comic Sans", 24, "bold")
SYMBOLS_FONT = ("Comic Sans", 24)

# Colors
DARK_BLUE = '#282A36'
WHITE = "#FFFFFF"
LIGHT_BLUE = "#44475A"
LIGHT_GRAY = "#A7A6BA"
LABEL_COLOR = "#000000"
BTN_COLOR = "#6272A4"

# Numbers
# Seven = hashlib.md5(Image.open('buttons/Seven.png'))
# Seven.update()

# note: crtl+/ will mass comment
# One = ih.average_hash(Image.open('buttons/One.png'))
# Two = ih.average_hash(Image.open('buttons/Two.png'))
# Three = ih.average_hash(Image.open('buttons/Three.png'))
# Four = ih.average_hash(Image.open('buttons/Four.png'))
# Five = ih.average_hash(Image.open('buttons/Five.png'))
# Six = ih.average_hash(Image.open('buttons/Six.png'))
# Seven = ih.average_hash(Image.open('buttons/Seven.png'))
# Eight = ih.average_hash(Image.open('buttons/Eight.png'))
# Nine = ih.average_hash(Image.open('buttons/Nine.png'))
# Zero = ih.average_hash(Image.open('buttons/Zero.png'))

class Calculator:
    def __init__(self):
        # Create window
        self.window = tk.Tk()
        self.window.geometry("350x500")
        # self.window.resizable(0, 0) # used to stop the window from being resized
        self.window.title("Calculator")

        # --trying to adjust frame color--
        # found out that this can't be changed and is only adjusted by
        # window settings
        # self.window.configure(bg="#000000")
        # frame_color = tk.Frame(self.window, bg='#000000')
        # frame_color.pack()

        # Create display
        self.total_expression = ""
        self.current_expression = ""
        self.display = self.display_frame()
        self.total, self.expression = self.create_display()

        # Create buttons
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        # This doesn't work, it only expects an iterable or a string
        # self.Digits = namedtuple("Digits", self.digits.keys())(*self.digits.values())
        # math symbols
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        # self.create_buttons_frame
        self.buttons_frame = self.buttons_frame()

        # Making the buttons fill into the screen
        for b in range(1, 5):
            self.buttons_frame.rowconfigure(b, weight=1)
            self.buttons_frame.columnconfigure(b, weight=1)

        # Buttons
        self.digit_buttons()
        self.operator_buttons()
        self.special_buttons()

        # button images ---unused ---
        # self.pngList = {
        #     1: "buttons/One.png", 2: "buttons/Two.png", 3: "buttons/Three.png",
        #     4: "buttons/Four.png", 5: "buttons/Five.png", 6: "buttons/Six.png",
        #     7: "buttons/Seven.png", 8: "buttons/Eight.png", 9: "buttons/Nine.png",
        #     0: "buttons/Zero.png"
        # }

    # Buttons
    def special_buttons(self):
        self.clear_button()
        self.equals_button()
        self.sqrt_button()
        self.square_button()

    # Adding operators to labels
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ''
        self.total_label()
        self.update_label()

    # Creating display for numbers and expression
    def display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    # Creating the display for equation total and equation expression
    def create_display(self):
        ttl = tk.Label(self.display, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                       fg=LABEL_COLOR, padx=24, font=TTL_FONT)
        ttl.pack(expand=True, fill="both")

        exp = tk.Label(self.display, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                       fg=LABEL_COLOR, padx=24, font=EXP_FONT)
        exp.pack(expand=True, fill="both")
        return ttl, exp

    # Add expression to label
    def add_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    # Creating grid for digit buttons
    def digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=digit, bg=WHITE, fg=BTN_COLOR,
                               font=DIGITS_FONT, borderwidth=0,
                               command=lambda dgt=digit: self.add_expression(dgt))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    # adding operator buttons to grid
    def operator_buttons(self):
        x = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=DARK_BLUE, fg=BTN_COLOR,
                               font=SYMBOLS_FONT, borderwidth=0,
                               command=lambda opt=operator: self.append_operator(opt))
            button.grid(row=x, column=4, sticky=tk.NSEW)
            x += 1

    # Clearing labels functionality
    def clear(self):
        self.current_expression = ''
        self.total_expression = ''
        self.update_label()
        self.total_label()

    # Adding clear button to grid
    def clear_button(self):
        button = tk.Button(self.buttons_frame, text="AC", bg=DARK_BLUE, fg=BTN_COLOR,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    # Squaring functionality
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    # Adding square button to grid
    def square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=DARK_BLUE, fg=BTN_COLOR,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    # Square root functionality
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**.5"))
        self.update_label()

    # Adding square root button to grid
    def sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=DARK_BLUE, fg=BTN_COLOR,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    # Adding current label to total label with exception handling ->
    # also provides functionality for equals sign
    def evaluate(self):
        self.total_expression += self.current_expression
        self.total_label()
        # Adding exception handling exceptions that won't compute
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ''
        except Exception as e:
            self.current_expression = "ERROR"
            # I used "ERROR" it resulted in "ERRORERROR", but with a blank string
            # it passed the error message and turned the total expression blank
            self.total_expression = ""
        self.update_label()

    # Adding equal sign button
    def equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=BTN_COLOR,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    # Buttons frame
    def buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    # Input expression into total
    def total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f'{symbol}')
        self.total.config(text=expression)

    # Updating Label
    def update_label(self):
        # updating the label and truncating it to 10
        self.expression.config(text=self.current_expression[:10])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()