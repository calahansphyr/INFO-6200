import tkinter as tk
from tkinter import messagebox, ttk


class Calculator:
    """A simple GUI calculator launched from the command line."""

    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title("Calculator")

        # Current expression shown in the display
        self.expression: str = ""
        self.display_text = tk.StringVar()

        self._build_layout()

    def _build_layout(self) -> None:
        """Create display and buttons."""
        entry = ttk.Entry(
            self.master,
            textvariable=self.display_text,
            font=("Arial", 20),
            justify="right",
        )
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        buttons = [
            "7",
            "8",
            "9",
            "/",
            "4",
            "5",
            "6",
            "*",
            "1",
            "2",
            "3",
            "-",
            "0",
            ".",
            "=",
            "+",
        ]

        row = 1
        col = 0
        for label in buttons:
            if label == "=":
                ttk.Button(self.master, text=label, command=self.calculate).grid(
                    row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2
                )
                col += 1
            else:
                ttk.Button(
                    self.master,
                    text=label,
                    command=lambda value=label: self.append(value),
                ).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

            col += 1
            if col > 3:
                col = 0
                row += 1

        ttk.Button(
            self.master,
            text="C",
            command=self.clear,
        ).grid(row=row, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

        # Make the grid responsive
        for i in range(row + 1):
            self.master.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.master.grid_columnconfigure(j, weight=1)

    def append(self, value: str) -> None:
        """Append a character to the expression."""
        self.expression += value
        self.display_text.set(self.expression)

    def calculate(self) -> None:
        """Evaluate the current expression with friendly error handling."""
        try:
            result = eval(self.expression)
            self.display_text.set(str(result))
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed.")
            self.clear()
        except Exception:
            messagebox.showerror("Error", "Please enter a valid number and operation.")
            self.clear()

    def clear(self) -> None:
        """Reset the display and expression."""
        self.expression = ""
        self.display_text.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
