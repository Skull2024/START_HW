from Calculator2 import Calculator
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    calc.create_gui()
    root.mainloop()