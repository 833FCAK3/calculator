import tkinter as tk
import tkinter.ttk as ttk
from functools import partial


class Calculator:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("400x500")

        self.display_label_1 = ttk.Label(text="")
        self.display_label_2 = ttk.Label(text="")

        self.plus_button = ttk.Button(text="+", command=partial(self.update_label, "+"))
        self.minus_button = ttk.Button(text="-", command=partial(self.update_label, "-"))
        self.divide_button = ttk.Button(text="÷", command=partial(self.update_label, "÷"))
        self.multiply_button = ttk.Button(text="×", command=partial(self.update_label, "×"))
        self.one_button = ttk.Button(text="1", command=partial(self.update_label, "1"))
        self.two_button = ttk.Button(text="2", command=partial(self.update_label, "2"))
        self.three_button = ttk.Button(text="3", command=partial(self.update_label, "3"))
        self.four_button = ttk.Button(text="4", command=partial(self.update_label, "4"))
        self.five_button = ttk.Button(text="5", command=partial(self.update_label, "5"))
        self.six_button = ttk.Button(text="6", command=partial(self.update_label, "6"))
        self.seven_button = ttk.Button(text="7", command=partial(self.update_label, "7"))
        self.eight_button = ttk.Button(text="8", command=partial(self.update_label, "8"))
        self.nine_button = ttk.Button(text="9", command=partial(self.update_label, "9"))
        self.zero_button = ttk.Button(text="0", command=partial(self.update_label, "0"))
        self.equal_button = ttk.Button(text="=", command=partial(self.update_label, "="))
        self.backspace_button = ttk.Button(text="◄", command=partial(self.update_label, "◄"))
        self.decimal_point_button = ttk.Button(text=".", command=partial(self.update_label, "."))
        self.clear_button = ttk.Button(text="C", command=partial(self.update_label, "C"))

        self.widgets = [
            self.display_label_1,
            self.display_label_2,
            self.plus_button,
            self.minus_button,
            self.divide_button,
            self.multiply_button,
            self.one_button,
            self.two_button,
            self.three_button,
            self.four_button,
            self.five_button,
            self.six_button,
            self.seven_button,
            self.eight_button,
            self.nine_button,
            self.zero_button,
            self.equal_button,
            self.backspace_button,
            self.decimal_point_button,
            self.clear_button,
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
        for widget in self.widgets:
            widget.pack()

    def render(self):
        self.pack_all()
        self.window.mainloop()
