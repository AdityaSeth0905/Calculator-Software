import customtkinter as ctk

class Cal:
    def __init__(self, num1, num2, sym):
        self.num1 = num1
        self.num2 = num2
        self.sym = sym
        self.function_map = {
            "+": self.add,
            "-": self.minus,
            "*": self.mul,
            "/": self.div,
            "%": self.mod
        }
    
    def add(self):
        return self.num1 + self.num2
    
    def minus(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def mod(self):
        return self.num1 % self.num2
    
    def div(self):
        return self.num1 / self.num2
    
    def call_function(self):
        if self.sym in self.function_map:
            return self.function_map[self.sym]()
        else:
            return "Invalid input"

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("400x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.current_input = ""
        self.operator = ""
        self.first_num = None

        # Display
        self.display = ctk.CTkEntry(root, font=("Arial", 24), width=350, height=50, corner_radius=10, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=20, padx=20)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, value, row, column):
        button = ctk.CTkButton(self.root, text=value, width=80, height=80, corner_radius=10, font=("Arial", 18),
                               command=lambda: self.button_click(value))
        button.grid(row=row, column=column, padx=10, pady=10)

    def button_click(self, value):
        if value.isdigit():
            self.current_input += value
            self.update_display()
        elif value in "+-*/%":
            self.operator = value
            self.first_num = float(self.current_input)
            self.current_input = ""
            self.update_display()
        elif value == "=":
            if self.first_num is not None and self.operator:
                second_num = float(self.current_input)
                calc = Cal(self.first_num, second_num, self.operator)
                result = calc.call_function()
                self.current_input = str(result)
                self.first_num = None
                self.operator = ""
                self.update_display()
        elif value == "C":
            self.clear()

    def update_display(self):
        self.display.delete(0, ctk.END)
        self.display.insert(0, self.current_input)

    def clear(self):
        self.current_input = ""
        self.first_num = None
        self.operator = ""
        self.update_display()

# Running the application
if __name__ == "__main__":
    root = ctk.CTk()
    app = CalculatorApp(root)
    root.mainloop()
