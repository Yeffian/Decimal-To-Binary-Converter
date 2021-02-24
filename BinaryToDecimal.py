# Python program to convert decimal to binary (and vice versa)
# Author: Yeffian the Teapot

exitCode = '.' # Declaring a exit code, which the user can input to stop the program

# Function to convert decimal to binary
def decimal_to_binary(n): 
    return bin(n).replace("0b", "") 

# Function to convert binary to decimal
def binary_to_decimal(n):
    return int(n, 2)
   
print("Welcome to my decimal to/from binary converter! Choose a mode: A: decimal to binary, B: binary to decimal")
# Infinite loop to check for input
while True:
    num = input("Enter the mode: ") # Asking for input
    if num == "A":
        num = int(input("Enter the decimal number you wish to convert:"))
        print(f"It's {decimal_to_binary(num)}!") # Printing the binary output
    elif num == "B":
        num = input("Enter the binary number you wish to convert:")
        print(f"It's {binary_to_decimal(num)}!") # Printing the decimal output
    else:
        print("Please choose between \"A\" and \"B.\"") # Printing that the mode is invalid
