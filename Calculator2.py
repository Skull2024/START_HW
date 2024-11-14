import math
import os
import tkinter as tk
from tkinter import messagebox
from operations import MathOperations
from history import HistoryManager

class Calculator:
    def __init__(self, root):
        self.math_operations = MathOperations()
        self.history_manager = HistoryManager()
        self.expression = ""
        self.current_operation = ""
        self.input_text = tk.StringVar()
        self.root = root

    def on_click(self, button_text):
        if button_text == "=":
            try:
                parts = self.expression.strip().split()
                if len(parts) == 3:
                    numbers = list(map(float, [parts[0], parts[2]]))
                elif len(parts) == 2 and self.current_operation == "sqrt":
                    numbers = [float(parts[1])]
                else:
                    raise ValueError("Некорректный ввод")

                if self.current_operation == "+":
                    result = self.math_operations.add(numbers)
                elif self.current_operation == "-":
                    result = self.math_operations.subtract(numbers)
                elif self.current_operation == "*":
                    result = self.math_operations.multiply(numbers)
                elif self.current_operation == "/":
                    result = self.math_operations.divide(numbers)
                elif self.current_operation == "^":
                    result = self.math_operations.power(numbers[0], numbers[1])
                elif self.current_operation == "%":
                    result = self.math_operations.percentage(numbers[0], numbers[1])
                elif self.current_operation == "sqrt":
                    result = self.math_operations.sqrt(numbers[0])
                else:
                    result = "Ошибка: неверная операция"
                
                self.history_manager.save_to_history(f"{self.expression} = {result}")
                self.expression = str(result)
                self.input_text.set(self.expression)
            except ValueError:
                messagebox.showerror("Ошибка", "Некорректный ввод. Пожалуйста, введите корректные числа.")
                self.expression = ""
                self.input_text.set("")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
                self.expression = ""
                self.input_text.set("")
        elif button_text == "C":
            self.expression = ""
            self.input_text.set("")
        elif button_text in ["+", "-", "*", "/", "^", "%", "sqrt"]:
            self.current_operation = button_text
            self.expression += f" {button_text} "
            self.input_text.set(self.expression)
        else:
            self.expression += button_text
            self.input_text.set(self.expression)

    def create_gui(self):
        self.root.title("Калькулятор")
        self.root.geometry("360x360")
        self.root.configure(bg="white")

        input_frame = tk.Frame(self.root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side="top")

        input_field = tk.Entry(input_frame, font=('tahoma', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify="center")
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        buttons_frame = tk.Frame(self.root, width=312, height=272.5, bg="white")
        buttons_frame.pack()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '^', '%', 'sqrt', 'C'
        ]

        row = 0
        col = 0
        for button in buttons:
            tk.Button(buttons_frame, text=button, width=12, height=3, bd=0, bg="#cd7f32", cursor="hand2",
                      command=lambda b=button: self.on_click(b)).grid(row=row, column=col, padx=1, pady=1)
            col += 1
            if col > 3:
                col = 0
                row += 1