import tkinter as tk

from conv import bin2hex

def convert():
    '''
    Button functions should be defined before the main loop starts, 
    so that they can be referenced by the buttons when they are created.
    '''
    binary = binary_entry.get()
    hexadecimal = bin2hex(binary)
    result_label.config(text=hexadecimal)

# Create the main window 
window = tk.Tk()
window.title("Binary to Hex")

# Create the input field
binary_entry = tk.Entry(window)
binary_entry.pack()

# Create the button and link it to the convert function
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack()

# Create the label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

"""
Start the main loop, GUI applications typically have a main loop 
that waits for user interaction. This loop should be the last thing 
in your script, after all widgets have been created and configured.
"""

window.mainloop()