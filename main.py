import tkinter as tk

# constants
LARGE_FONT = ("Comic Sans", 40, "bold")
SMALL_FONT = ("Comic Sans", 16)
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#19BDFF"

class Calculator:
    def __init__(self):
        # Create window
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        # Create display
        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = self.create_display()
        self.total, self.expression = self.create_display_frame()

        # Create buttons
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        # this errored out because button_frame needed to be above
        # self.create_buttons_frame
        # Note for error doc:
        # if you assign an attribute to a method, if but be assigned above the method
        self.buttons_frame = self.create_buttons_frame()
        self.create_digit_buttons()

    def create_display(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_frame(self):
        total = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=SMALL_FONT)
        total.pack(expand=True, fill="both")

        expression = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                              fg=LABEL_COLOR, padx=24, font=LARGE_FONT)
        expression.pack(expand=True, fill="both")
        return total, expression

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()






