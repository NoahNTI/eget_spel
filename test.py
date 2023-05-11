import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.resizable(False, False)

        # Create input field
        self.input_field = tk.Entry(master, width=40, justify="right")
        self.input_field.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create number buttons
        self.create_button(1, 1)
        self.create_button(2, 1)
        self.create_button(3, 1)
        self.create_button(4, 1)
        self.create_button(5, 2)
        self.create_button(6, 2)
        self.create_button(7, 2)
        self.create_button(8, 2)
        self.create_button(9, 3)
        self.create_button(0, 3)

        # Create operation buttons
        self.create_button("+", 4)
        self.create_button("-", 4)
        self.create_button("*", 4)
        self.create_button("/", 4)
        self.create_button("C", 3)
        self.create_button("=", 4)

    def create_button(self, text, row):
        button = tk.Button(self.master, text=text, width=9, height=4, command=lambda: self.button_click(text))
        button.grid(row=row, column=self.get_column(text), padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.input_field.delete(0, tk.END)
        elif text == "=":
            try:
                result = str(eval(self.input_field.get()))
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, result)
            except:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, "Error")
        else:
            self.input_field.insert(tk.END, text)

    def get_column(self, text):
        if text in ("+", "-", "*", "/"):
            return 3
        elif text == "0":
            return 1
        elif text in ("1", "2", "3"):
            return 0
        elif text in ("4", "5", "6"):
            return 1
        else:
            return 2


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
