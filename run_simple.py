import conv
import sys

# Print app title ...
print("Welcome to the calculator program!")

# Get the binary number from the user
binary = input("Enter a binary number: ")
# Convert the binary number to hexadecimal
hexadecimal = conv.bin2hex(binary)

# Print the result using an f-string for formatting (simpler to manage)
print(f"The hexadecimal representation of {binary} is {hexadecimal}.")
# Print using concatenation (required for exam)
print("The hexadecimal representation of " + binary + " is " + hexadecimal + ".")