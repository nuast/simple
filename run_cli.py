import conv
import sys

'''
This allows the user to run the program from the command line and 
optionally provide a binary number as an argument. If no argument 
is provided, it will prompt the user for input.

TASK 1 : The user might like to change which conversion is performed. 
For example, they might want to convert from decimal to binary instead 
of binary to hexadecimal. To accommodate this, you could modify the 
program to accept a second command-line argument that specifies the 
type of conversion.
'''


print("Welcome to the calculator program!")

# Check if a command-line argument was provided
if len(sys.argv) == 2:
    binary = sys.argv[1]
else:
    binary = input("Enter a binary number: ")

hexadecimal = conv.bin2hex(binary)
print(f"The hexadecimal representation of {binary} is {hexadecimal}.")