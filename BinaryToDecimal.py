# Python program to convert decimal to binary
# Author: Yeffian the Teapot   

num = 0 # Declaring a num variable to check and store input
exitCode = 1 # Declaring a exit code, which the user can input to stop the program


# Function to convert decimal to binary
def decimalToBinary(n): 
    return bin(n).replace("0b", "") 
   

# Infinite loop to check for input
while True:
    if num == exitCode:   # Checking if the input is the exit code
        print("Goodbye!")
        break # Using the 'break' keyword to break out of the loop
    # If the input is not the exit code
    num = int(input("Enter a binary number: "))  # Asking for input
    print(decimalToBinary(num))  # Printing the binary output
