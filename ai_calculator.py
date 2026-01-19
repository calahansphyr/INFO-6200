import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.expression = ""
        self.entry_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry field
        entry = ttk.Entry(self.master, textvariable=self.entry_text, font=('Arial', 20), justify='right')
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            if button == '=':
                ttk.Button(self.master, text=button, command=self.calculate).grid(row=row, column=col, columnspan=2, sticky='nsew')
                col += 1
            else:
                ttk.Button(self.master, text=button, command=lambda b=button: self.press(b)).grid(row=row, column=col, sticky='nsew')

            col += 1
            if col > 3:
                col = 0
                row += 1

        ttk.Button(self.master, text='C', command=self.clear).grid(row=row, column=0, columnspan=4, sticky='nsew')

    def press(self, key):
        self.expression += str(key)
        self.entry_text.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.entry_text.set(result)
            self.expression = result
        except:
            self.entry_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.entry_text.set("")

if __name__ == '__main__':
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()