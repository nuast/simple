import tkinter as tk
from cs import bin2hex

def is_binary(value):
    return value != "" and all(digit in "01" for digit in value)

def convert():
    binary = binary_entry.get()

    if is_binary(binary):
        hexadecimal = bin2hex(binary)
        result_var.set(hexadecimal.upper())
    else:
        result_var.set("Invalid binary number")

window = tk.Tk()
window.title("Binary to Hex Converter")
window.geometry("320x160")
window.resizable(False, False)

tk.Label(window, text="Binary → Hex Converter", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=(10, 5))
tk.Label(window, text="Binary:").grid(row=1, column=0, sticky="e", padx=5, pady=5)

binary_entry = tk.Entry(window, width=25)
binary_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(window, text="Convert", command=convert, width=15).grid(row=2, column=0, columnspan=3, pady=10)
tk.Label(window, text="Hex:").grid(row=3, column=0, sticky="e", padx=5)

result_var = tk.StringVar()
tk.Label(window, textvariable=result_var, fg="blue").grid(row=3, column=1, sticky="w", padx=5)

window.mainloop()