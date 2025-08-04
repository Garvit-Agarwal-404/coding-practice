import tkinter as tk

# Function to handle button clicks
def button_click(symbol):
    if symbol == '=':
        try:
            result = eval(entry.get())  # Evaluate the expression in the entry widget
            entry.delete(0, tk.END)     # Clear the entry widget
            entry.insert(tk.END, str(result))  # Display the result
        except Exception as e:
            entry.delete(0, tk.END)     # Clear the entry widget
            entry.insert(tk.END, "Error")  # Display error message
    elif symbol == 'C':
        entry.delete(0, tk.END)     # Clear the entry widget
    else:
        entry.insert(tk.END, symbol)  # Append the clicked symbol to the entry widget

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget
entry = tk.Entry(root, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create buttons
row, col = 1, 0
for symbol in buttons:
    tk.Button(root, text=symbol, width=5, height=2, font=('Arial', 12),
              command=lambda s=symbol: button_click(s)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the tkinter event loop
root.mainloop()
