# By: Noah Schlaupitz
# Calculator App

import tkinter as tk
import numpy

# Fonts
EXP_FONT = ("Comic Sans", 48, "bold")
TTL_FONT = ("Comic Sans", 16)
DIGITS_FONT = ("Comic Sans", 24, "bold")
SYMBOLS_FONT = ("Comic Sans", 24)

# Colors
DARK_BLUE = '#282A36'
WHITE = "#FFFFFF"
LIGHT_BLUE = "#44475A"
LIGHT_GRAY = "#D4D4D2"
DARK_GRAY = "#505050"
DARK_GRAY2 = "#414141"
LABEL_COLOR = "#000000"
BTN_COLOR = "#6272A4"
BLACK_COLOR = "#1C1C1C"
ORANGE = "#FF9500"

class Calculator:
    def __init__(self):
        # Create window
        self.window = tk.Tk()
        self.window.geometry("600x600")
        self.window.resizable(0, 0) # used to stop the window from being resized
        self.window.title("Calculator")

        # Create display
        self.total_expression = ""
        self.current_expression = ""
        self.display = self.display_frame()
        self.total, self.expression = self.create_display()

        # Create buttons
        self.digits = {
            7: (1, 3), 8: (1, 4), 9: (1, 5),
            4: (2, 3), 5: (2, 4), 6: (2, 5),
            1: (3, 3), 2: (3, 4), 3: (3, 5),
            '.': (4, 4), 0: (4, 3)
        }

        self.digits_png = ["buttons/Seven.png", "buttons/Eight.png", "buttons/Nine.png",
                           "buttons/Four.png", "buttons/Five", "buttons/Six.png",
                           "button/One.png", "buttons/Two.png", "buttons/One.png",
                           "buttons/Zero.png"]

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
        # self.digit_buttons_png()

    # Buttons
    def special_buttons(self):
        self.clear_button()
        self.equals_button()
        self.sqrt_button()
        self.square_button()
        self.percent_button()
        self.negative_button()
        # self.grid_button()
        self.cube_button()
        self.cuberoot_button()
        self.one_over_x_button()
        self.pi_button()
        self.ten_to_x_button()
        self.factorial_button()
        self.log_ten_button()
        self.e_to_x_button()

    # Adding operators to labels
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ''
        self.total_label()
        self.update_label()

    # Creating display for numbers and expression
    def display_frame(self):
        frame = tk.Frame(self.window, height=221)
        frame.pack(expand=True, fill="both")
        return frame

    # Creating the display for equation total and equation expression
    def create_display(self):
        ttl = tk.Label(self.display, text=self.total_expression, anchor=tk.E, bg=BLACK_COLOR,
                       fg=WHITE, padx=24, font=TTL_FONT)
        ttl.pack(expand=True, fill="both")

        exp = tk.Label(self.display, text=self.current_expression, anchor=tk.E, bg=BLACK_COLOR,
                       fg=WHITE, padx=24, font=EXP_FONT)
        exp.pack(expand=True, fill="both")
        return ttl, exp

    # Add expression to label
    def add_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    # Creating grid for digit buttons
    def digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=digit, bg=DARK_GRAY, fg=WHITE,
                               font=DIGITS_FONT, borderwidth=0,
                               command=lambda dgt=digit: self.add_expression(dgt),
                               height=1, width=1)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    # adding operator buttons to grid
    def operator_buttons(self):
        x = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=ORANGE, fg=WHITE,
                               font=SYMBOLS_FONT, borderwidth=0,
                               command=lambda opt=operator: self.append_operator(opt),
                               height=1, width=6)
            button.grid(row=x, column=6, sticky=tk.NSEW)
            x += 1

    # percent functionality
    def percent(self):
        self.current_expression = str(eval(f"{self.current_expression}*.01"))
        self.update_label()

    # Percent Button
    def percent_button(self):
        button = tk.Button(self.buttons_frame, text="%", bg=LIGHT_GRAY, fg=BLACK_COLOR,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.percent, height=1, width=5)
        button.grid(row=0, column=5, sticky=tk.NSEW)

    # +/- functionality
    def negative(self):
        self.current_expression = str(eval(f"{self.current_expression}*-1"))
        self.update_label()

    # +/- button
    def negative_button(self):
        button = tk.Button(self.buttons_frame, text='+/-', bg=LIGHT_GRAY, fg=BLACK_COLOR,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.negative, height=1, width=1)
        button.grid(row=0, column=4, sticky=tk.NSEW)

    # Clearing labels functionality
    def clear(self):
        self.current_expression = ''
        self.total_expression = ''
        self.update_label()
        self.total_label()

    # Adding clear button to grid
    def clear_button(self):
        button = tk.Button(self.buttons_frame, text="AC", bg=LIGHT_GRAY, fg=BLACK_COLOR,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.clear, height=1, width=1)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    # Squaring functionality
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    # Adding square button to grid
    def square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=DARK_GRAY2, fg=WHITE,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.square, height=1, width=1)
        button.grid(row=1, column=1, sticky=tk.NSEW)

    # Square root functionality
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**.5"))
        self.update_label()

    # Adding square root button to grid
    def sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=DARK_GRAY2, fg=WHITE,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.sqrt, height=1, width=1)
        button.grid(row=1, column=2, sticky=tk.NSEW)

    # Cube functionality
    def cuberoot(self):
        self.current_expression = str(eval(f"{self.current_expression}**(1/3)"))
        self.update_label()

    # Cube button
    def cuberoot_button(self):
        button = tk.Button(self.buttons_frame, text="\u221bx", bg=DARK_GRAY2, fg=WHITE,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.cuberoot, height=1, width=1)
        button.grid(row=2, column=2, sticky=tk.NSEW)

    # Cube functionality
    def cube(self):
        self.current_expression = str(eval(f"{self.current_expression}**3"))
        self.update_label()

    # Cube button
    def cube_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b3", bg=DARK_GRAY2, fg=WHITE,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.cube, height=1, width=1)
        button.grid(row=2, column=1, sticky=tk.NSEW)

    # 1/x functionality
    def one_over_x(self):
        self.current_expression = str(eval(f"1/{self.current_expression}"))
        self.update_label()

    # 1/x button
    def one_over_x_button(self):
        button = tk.Button(self.buttons_frame, text="1/x", bg=DARK_GRAY2, fg=WHITE,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.one_over_x, height=1, width=1)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    # Pi functionality
    def pi(self):
        self.current_expression = str(numpy.pi)
        self.update_label()

    # Pi button
    def pi_button(self):
        button = tk.Button(self.buttons_frame, text="Pi", bg=DARK_GRAY2, fg=WHITE,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.pi, height=1, width=1)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    # 10^x functionality
    def ten_to_x(self):
        self.current_expression = str(eval(f"10**{self.current_expression}"))
        self.update_label()

    # 10^x button
    def ten_to_x_button(self):
        button = tk.Button(self.buttons_frame, text="10\u02e3", bg=DARK_GRAY2, fg=WHITE,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.ten_to_x, height=1, width=1)
        button.grid(row=3, column=1, sticky=tk.NSEW)

    # Factorial functionality
    def factorial(self):
        self.current_expression = str(eval(f"math.factorial({self.current_expression})"))
        self.update_label()

    # Factorial button
    def factorial_button(self):
        button = tk.Button(self.buttons_frame, text="x!", bg=DARK_GRAY2, fg=WHITE,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.factorial, height=1, width=1)
        button.grid(row=3, column=2, sticky=tk.NSEW)

    # Log10 functionality
    def log_ten(self):
        self.current_expression = str(eval(f"math.log({self.current_expression})"))
        self.update_label()

    # Log10 button
    def log_ten_button(self):
        button = tk.Button(self.buttons_frame, text="log10", bg=DARK_GRAY2, fg=WHITE,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.factorial, height=1, width=1)
        button.grid(row=4, column=1, sticky=tk.NSEW)

    # e^x functionality
    def e_to_x(self):
        self.current_expression = str(eval(f"math.exp({self.current_expression})"))
        self.update_label()

    # e^x button
    def e_to_x_button(self):
        button = tk.Button(self.buttons_frame, text="e\u02e3", bg=DARK_GRAY2, fg=WHITE,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.e_to_x, height=1, width=1)
        button.grid(row=4, column=2, sticky=tk.NSEW)

    # Adding current label to total label with exception handling ->
    # also provides functionality for equals sign
    def evaluate(self):
        self.total_expression += self.current_expression
        self.total_label()
        # x = "{:2.E}".format(Decimal(self.total_expression))
        # Adding exception handling exceptions that won't compute
        try:
            self.current_expression = (str(eval(self.total_expression)))
            self.total_expression = ''
        except Exception as e:
            self.current_expression = "ERROR"
            # I used "ERROR" it resulted in "ERRORERROR", but with a blank string
            # it passed the error message and turned the total expression blank
            self.total_expression = ""
        self.update_label()

    # Adding equal sign button
    def equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=ORANGE, fg=WHITE,
                           font=SYMBOLS_FONT, borderwidth=0,
                           command=self.evaluate, height=1, width=1)
        button.grid(row=4, column=5, columnspan=2, sticky=tk.NSEW)

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
        self.expression.config(text=self.current_expression[:16])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
