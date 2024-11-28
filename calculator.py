import itertools
import tkinter as tk
import tkinter.ttk as ttk
from functools import partial


class Calculator:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("450x500")
        self.frame = tk.Frame(self.window)

        self.display_label_1 = ttk.Label(text="")
        self.display_label_2 = ttk.Label(text="")

        self.plus_button = ttk.Button(self.frame, text="+", command=partial(self.update_label, "+"))
        self.minus_button = ttk.Button(self.frame, text="-", command=partial(self.update_label, "-"))
        self.divide_button = ttk.Button(self.frame, text="÷", command=partial(self.update_label, "÷"))
        self.multiply_button = ttk.Button(self.frame, text="×", command=partial(self.update_label, "×"))
        self.one_button = ttk.Button(self.frame, text="1", command=partial(self.update_label, "1"))
        self.two_button = ttk.Button(self.frame, text="2", command=partial(self.update_label, "2"))
        self.three_button = ttk.Button(self.frame, text="3", command=partial(self.update_label, "3"))
        self.four_button = ttk.Button(self.frame, text="4", command=partial(self.update_label, "4"))
        self.five_button = ttk.Button(self.frame, text="5", command=partial(self.update_label, "5"))
        self.six_button = ttk.Button(self.frame, text="6", command=partial(self.update_label, "6"))
        self.seven_button = ttk.Button(self.frame, text="7", command=partial(self.update_label, "7"))
        self.eight_button = ttk.Button(self.frame, text="8", command=partial(self.update_label, "8"))
        self.nine_button = ttk.Button(self.frame, text="9", command=partial(self.update_label, "9"))
        self.zero_button = ttk.Button(self.frame, text="0", command=partial(self.update_label, "0"))
        self.equal_button = ttk.Button(self.frame, text="=", command=partial(self.update_label, "="))
        self.backspace_button = ttk.Button(self.frame, text="◄", command=partial(self.update_label, "◄"))
        self.decimal_point_button = ttk.Button(self.frame, text=".", command=partial(self.update_label, "."))
        self.clear_button = ttk.Button(self.frame, text="C", command=partial(self.update_label, "C"))

        self.labels = [self.display_label_1, self.frame]

        self.buttons = [
            self.seven_button,
            self.eight_button,
            self.nine_button,
            self.divide_button,
            self.four_button,
            self.five_button,
            self.six_button,
            self.multiply_button,
            self.one_button,
            self.two_button,
            self.three_button,
            self.minus_button,
            self.backspace_button,
            self.zero_button,
            self.decimal_point_button,
            self.plus_button,
            self.clear_button,
            self.equal_button,
        ]

    # methods
    def update_label(self, value: str) -> None:
        match value:
            case "◄":
                self.display_label_1.config(text=self.display_label_1.cget("text")[:-1])
            case "=":
                expression = self.display_label_1.cget("text")
                expression = expression.replace("÷", "/")
                expression = expression = expression.replace("×", "*")
                self.display_label_1.config(text=str(eval(expression)))
            case "C":
                self.display_label_1.config(text="")
            case _:
                self.display_label_1.config(text=self.display_label_1.cget("text") + value)

    def pack_all(self):
        for label in self.labels:
            label.pack(pady=8)

    def grid_all(self):
        rows = list(itertools.product([_ for _ in range(5)], [_ for _ in range(4)]))
        rows[-4] = list(rows[-4])
        rows[-3] = list(rows[-3])
        rows[-4][1] = rows[-4][1] + 2
        rows[-3][1] = rows[-3][1] + 2
        
        for button, row_ in zip(self.buttons, rows):
            print(button, row_)
            button.grid(row=row_[0], column=row_[1])

    def render(self):
        self.pack_all()
        self.grid_all()
        self.window.mainloop()
