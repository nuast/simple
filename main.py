import tkinter as tk
from cs import (
    den2bin, den2hex, den2oct,
    bin2den, bin2hex, bin2oct,
    hex2den, hex2bin, hex2oct,
    oct2den
)

conversions = {
    "Denary → Binary": den2bin,
    "Denary → Hex": den2hex,
    "Denary → Octal": den2oct,
    "Binary → Denary": bin2den,
    "Binary → Hex": bin2hex,
    "Binary → Octal": bin2oct,
    "Hex → Denary": hex2den,
    "Hex → Binary": hex2bin,
    "Hex → Octal": hex2oct,
    "Octal → Denary": oct2den
}


def convert():
    number = number_entry.get()
    conversion = conversion_var.get()

    try:
        if conversion.startswith("Denary"):
            number = int(number)

        answer = conversions[conversion](number)
        result_var.set(str(answer).upper())

    except Exception:
        result_var.set("Invalid input")


window = tk.Tk()
window.title("Conversion App")
window.geometry("340x210")
window.resizable(False, False)

tk.Label(
    window,
    text="Number Conversion App",
    font=("Arial", 12, "bold")
).grid(row=0, column=0, columnspan=2, pady=(10, 5))

tk.Label(window, text="Conversion:").grid(
    row=1, column=0, sticky="e", padx=5, pady=5
)

conversion_var = tk.StringVar(value="Binary → Hex")
tk.OptionMenu(window, conversion_var, *conversions).grid(
    row=1, column=1, sticky="w", padx=5, pady=5
)

tk.Label(window, text="Number:").grid(
    row=2, column=0, sticky="e", padx=5, pady=5
)

number_entry = tk.Entry(window, width=25)
number_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(
    window,
    text="Convert",
    command=convert,
    width=15
).grid(row=3, column=0, columnspan=2, pady=10)

tk.Label(window, text="Result:").grid(
    row=4, column=0, sticky="e", padx=5
)

result_var = tk.StringVar()
tk.Label(
    window,
    textvariable=result_var,
    fg="blue"
).grid(row=4, column=1, sticky="w", padx=5)

window.mainloop()