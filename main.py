import tkinter as tk
import tkinter.ttk as ttk
from functools import partial


# Element definitions
window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

display_label_1 = ttk.Label(text="")
display_label_2 = ttk.Label(text="")
input_window = ttk.Entry()


# functions
def update_label(value: str) -> None:
    match value:
        case "◄":
            display_label_1.config(text=display_label_1.cget("text")[:-1])
        case "=":
            expression = display_label_1.cget("text")
            expression = expression.replace("÷", "/")
            expression = expression = expression.replace("×", "*")
            display_label_1.config(text=str(eval(expression)))
        case "C":
            display_label_1.config(text="")
        case _:
            display_label_1.config(text=display_label_1.cget("text") + value)


plus_button = ttk.Button(text="+", command=partial(update_label, "+"))
minus_button = ttk.Button(text="-", command=partial(update_label, "-"))
divide_button = ttk.Button(text="÷", command=partial(update_label, "÷"))
multiply_button = ttk.Button(text="×", command=partial(update_label, "×"))
one_button = ttk.Button(text="1", command=partial(update_label, "1"))
two_button = ttk.Button(text="2", command=partial(update_label, "2"))
three_button = ttk.Button(text="3", command=partial(update_label, "3"))
four_button = ttk.Button(text="4", command=partial(update_label, "4"))
five_button = ttk.Button(text="5", command=partial(update_label, "5"))
six_button = ttk.Button(text="6", command=partial(update_label, "6"))
seven_button = ttk.Button(text="7", command=partial(update_label, "7"))
eight_button = ttk.Button(text="8", command=partial(update_label, "8"))
nine_button = ttk.Button(text="9", command=partial(update_label, "9"))
zero_button = ttk.Button(text="0", command=partial(update_label, "0"))
equal_button = ttk.Button(text="=", command=partial(update_label, "="))
backspace_button = ttk.Button(text="◄", command=partial(update_label, "◄"))
decimal_point_button = ttk.Button(text=".", command=partial(update_label, "."))
clear_button = ttk.Button(text="C", command=partial(update_label, "C"))

# All packings
display_label_1.pack()
display_label_2.pack()
plus_button.pack()
minus_button.pack()
divide_button.pack()
multiply_button.pack()
one_button.pack()
two_button.pack()
three_button.pack()
four_button.pack()
five_button.pack()
six_button.pack()
seven_button.pack()
eight_button.pack()
nine_button.pack()
zero_button.pack()
equal_button.pack()
backspace_button.pack()
decimal_point_button.pack()
clear_button.pack()


window.mainloop()
