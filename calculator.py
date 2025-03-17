

import tkinter as tk
from tkinter import ttk
from fractions import Fraction

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Label for the Tab Name - changing text to "Option"
        self.tab_label = ttk.Label(root, text="Option", font=("Helvetica", 12, "bold"), width=15)  # Tab name set to "Option"
        self.tab_label.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        self.tab_label.config(background="lightblue", foreground="darkblue")  # Background and text color
        
        # Fraction selection Combobox inside the options tab
        self.fraction_option = ttk.Combobox(root, values=["1/2", "3/4", "2/3"], state='readonly', font=("Arial", 10), width=10)
        self.fraction_option.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")  # Make the combobox smaller
        self.fraction_option.bind("<<ComboboxSelected>>", self.select_fraction)

        # Entry field for displaying numbers
        self.display = ttk.Entry(root, justify="right", font=("Arial", 30))  # Larger font for mobile display
        self.display.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Calculator buttons
        buttons = [
            'AC', '%', 'C', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', '+'
        ]

        # Add buttons to the grid
        row = 2
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(root, text=button, command=cmd, style='TButton').grid(
                row=row, column=col, padx=5, pady=5, sticky="nsew"
            )
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Configure grid weights
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        root.grid_rowconfigure(5, weight=1)  # Set the last row weight to 1, same as the previous row
        for i in range(5):
            root.grid_columnconfigure(i, weight=1)

        # Customize button style for better touch areas
        style = ttk.Style()
        style.configure('TButton', font=("Arial", 20), padding=10)  # Increase padding for larger buttons

    def select_fraction(self, event):
        ''' Function to handle fraction selection from the Combobox '''
        fraction_input = self.fraction_option.get()
        if fraction_input:
            # Update display with selected fraction
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(Fraction(fraction_input)))

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == 'AC':
            self.display.delete(0, tk.END)
        elif key == 'C':
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])
        elif key == '%':
            try:
                value = float(self.display.get())
                result = value / 100
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, key)

def main():
    root = tk.Tk()
    root.geometry("360x640")  # Optimize window size for mobile devices
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
