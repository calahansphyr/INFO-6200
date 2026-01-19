import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=20, font=('Arial', 24), borderwidth=5, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Configure grid to be responsive
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

        # Create Number Buttons
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)

        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)

        self.create_button("0", 4, 0, columnspan=2)

        # Create Operator and Action Buttons
        self.create_button("+", 1, 3, command=lambda: self.on_operator_click('+'))
        self.create_button("-", 2, 3, command=lambda: self.on_operator_click('-'))
        self.create_button("*", 3, 3, command=lambda: self.on_operator_click('*'))
        self.create_button("/", 4, 3, command=lambda: self.on_operator_click('/'))

        self.create_button("C", 4, 2, command=self.on_clear_click)
        self.create_button("=", 5, 0, columnspan=4, command=self.on_equals_click)


    def create_button(self, text, row, col, columnspan=1, command=None):
        if command is None:
            command = lambda: self.on_number_click(text)
        button = tk.Button(self.master, text=text, font=('Arial', 18), command=command)
        button.grid(row=row, column=col, columnspan=columnspan, sticky="nsew", padx=5, pady=5)


    def on_number_click(self, number):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + str(number))

    def on_operator_click(self, operator):
        current = self.display.get()
        # Avoid multiple operators
        if current and current[-1] in "+-*/":
            return
        self.display.insert(tk.END, operator)

    def on_clear_click(self):
        self.display.delete(0, tk.END)

    def on_equals_click(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except (SyntaxError, ZeroDivisionError, TypeError):
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

if __name__ == '__main__':
    root = tk.Tk()
    my_gui = Calculator(root)
    root.mainloop()