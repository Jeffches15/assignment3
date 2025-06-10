""" 
This file is the "app/calculator.py" file. It contains a simple calculator that can add, subtract, multiply, 
and divide numbers based on what the user types.
"""

# We are importing the class Operations from "operations.py"
# we will use the 4 static methods from class Operations below
from app.operations import Operations

# main function called calculator
def calculator():
    # this line below is a doc string, used for documentation
    """Basic REPL calculator that performs addition, subtraction, multiplication, and division."""
    
    # First, we print a message to welcome the user to the calculator.
    print("Welcome to the calculator REPL! Type 'exit' to quit")

    while True:
        # asks for user input
        # will get operation (ex: "add") and two numbers from the user
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: ")
        
        # checks if user typed 'exit'
        # if user typed exit, stop program
        if user_input.lower() == "exit":
            print("Exiting calculator")
            break # 'break' command tells program to stop running loop and exit

        try:
            # now we split the user input into 3 parts: the operation and the two numbers
            # split() splits the user input into a list of words by separating the string at each space
            operation, num1, num2 = user_input.split()

            # convert num1 and num2 into floats
            num1, num2 = float(num1), float(num2)

        # if the user types something incorrectly, show an error
        except ValueError:
            print("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue # 'continue' means: try again by going back to the top of the loop

        # now we check what operation the user asked for and call the right function (addition, subtraction, etc.)
        if operation == "add":
            result = Operations.addition(num1, num2) # addition function to add numbers
        elif operation == "subtract":
            result = Operations.subtraction(num1, num2) # subtraction function to subtract numbers
        elif operation == "multiply":
            result = Operations.multiplication(num1, num2) # multiply function to multiply numbers
        elif operation == "divide":
            try:
                result = Operations.division(num1, num2) # division function to divide numbers
            except ValueError as e:
                # handles case when someone tries to divide by zero, which we can't do
                # division function will throw an error if someone tries to divide by zero
                    # and we catch that error here
                print(e)
                continue # go back to top of loop and try again
        else:
            # if someone types in unknown operation, show them this message.
            # The f before the string makes it an f-string (formatted string literal) in Python.
            # It allows you to embed variables or expressions directly into a string using curly braces {}.
            print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide")
            continue # go back to top of loop and try again
        
        print(f"Result: {result}")

# Explanation of __init__.py:
# In Python, a file named "__init__.py" is really important. It tells Python that the folder it's in (in this case, "calculator") 
# is a special kind of folder called a "package". Think of a package like a folder that contains related code, like a toolbox with
# different tools inside.
# 
# Without the "__init__.py" file, Python won't know that the folder can be used to group code together. It’s like a flag that says,
# "Hey Python, this folder can be used to import code!"
# 
# For example, if we put the "__init__.py" file in the "calculator" folder, we can import anything inside it by saying something like:
# "from app.calculator import calculator". The "__init__.py" file can be empty, or it can have code in it, but its main job is just 
# to make the folder a package.