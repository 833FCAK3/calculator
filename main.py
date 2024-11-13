import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title("Calculator")
window.geometry("400x500+500+100")

greeting = ttk.Label(text="Hello, Tkinter")
greeting.pack()



input_window = ttk.Entry()
input_window.pack()

#functions
def retrieve_text():
    inp = input_window.get()
    print(inp)

plus_button = ttk.Button(text="+", command=retrieve_text)
plus_button.pack()

print(window.pack_slaves())

window.mainloop()
