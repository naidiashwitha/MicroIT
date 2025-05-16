import tkinter as tk

class RealTimeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""

        # Display field
        self.input_text = tk.StringVar()
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        self.input_field = tk.Entry(
            self.input_frame, font=('arial', 18, 'bold'),
            textvariable=self.input_text, justify='right',
            bd=10, relief=tk.RIDGE
        )
        self.input_field.grid(row=0, column=0, ipadx=8, ipady=20, columnspan=4)

        # Buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(
                    self.root, text=text, fg='white', bg='green',
                    font=('arial', 14), height=2, width=6, command=self.evaluate
                )
            elif text == 'C':
                btn = tk.Button(
                    self.root, text=text, fg='white', bg='red',
                    font=('arial', 14), height=2, width=26, command=self.clear
                )
                btn.grid(row=row, column=0, columnspan=4, padx=5, pady=5)
                continue
            else:
                btn = tk.Button(
                    self.root, text=text, font=('arial', 14),
                    height=2, width=6,
                    command=lambda t=text: self.append_expression(t)
                )
            btn.grid(row=row, column=col, padx=5, pady=5)

    def append_expression(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            self.input_text.set("Cannot divide by 0")
            self.expression = ""
        except:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.input_text.set("")

# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    RealTimeCalculator(root)
    root.mainloop()
