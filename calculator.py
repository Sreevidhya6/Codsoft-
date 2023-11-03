import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            result.set(num1 / num2)
    except:
        result.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

entry_num1 = tk.Entry(root)
entry_num1.pack(side=tk.LEFT)

operation_var = tk.StringVar()
operation_choices = ["+", "-", "*", "/"]
operation_var.set("+")
operation_menu = tk.OptionMenu(root, operation_var, *operation_choices)
operation_menu.pack(side=tk.LEFT)

entry_num2 = tk.Entry(root)
entry_num2.pack(side=tk.LEFT)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

root.mainloop()