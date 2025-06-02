import tkinter as tk
import math

# Functions
def press(key):
    current = entry.get()
    if current == "Error":
        current = ""
    entry.delete(0, tk.END)
    entry.insert(0, current + str(key))

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def percent():
    try:
        result = float(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square():
    try:
        result = float(entry.get()) ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square_root():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sin_func():
    try:
        result = math.sin(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def cos_func():
    try:
        result = math.cos(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def tan_func():
    try:
        result = math.tan(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Keyboard input
def key_press(event):
    key = event.char
    if key in '0123456789.+-*/':
        press(key)
    elif key == '\r':
        equal()
    elif key == '\x08':
        backspace()

# GUI Setup
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg='#2e2e2e')

entry = tk.Entry(root, width=25, borderwidth=3, font=('Arial', 20), justify='right', bg='#1e1e1e', fg='white')
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Standard and scientific buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('√', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('x²', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('%', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('⌫', 4, 4),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2)
]

# Create buttons with appropriate commands
for (text, row, col) in buttons:
    if text == '=':
        cmd = equal
        color = '#4CAF50'
    elif text == '⌫':
        cmd = backspace
        color = '#f44336'
    elif text == '%':
        cmd = percent
        color = '#2196F3'
    elif text == 'x²':
        cmd = square
        color = '#2196F3'
    elif text == '√':
        cmd = square_root
        color = '#2196F3'
    elif text == 'sin':
        cmd = sin_func
        color = '#673AB7'
    elif text == 'cos':
        cmd = cos_func
        color = '#673AB7'
    elif text == 'tan':
        cmd = tan_func
        color = '#673AB7'
    else:
        cmd = lambda t=text: press(t)
        color = '#424242'
    
    tk.Button(root, text=text, width=5, height=2, font=('Arial', 16),
              bg=color, fg='white', command=cmd).grid(row=row, column=col, padx=3, pady=3)

# Clear button
tk.Button(root, text='C', width=16, height=2, font=('Arial', 16),
          bg='red', fg='white', command=clear).grid(row=5, column=3, columnspan=2, pady=10)

# Enable keyboard input
root.bind('<Key>', key_press)

# Start the app
root.mainloop()
