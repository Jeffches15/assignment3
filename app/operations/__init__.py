# this file is now called operations.py
# contains a class called Operations with 4 static methods
    # addition
    # subtraction
    # multiplication
    # division

class Operations:
    """
    The Operations class serves as a container for basic math operations
    By using static methods, we can perform these operations without needing to
        create an instance of the class
    """

    @staticmethod
    def addition(num1: float, num2: float) -> float:
        """
            takes num1 and num2 and returns their sum (num1 + num2)
            num1 and num2 are numbers with decimal points
            the return value is a number with decimals (a float)
        """

        return num1 + num2
    
    @staticmethod
    def subtraction(num1: float, num2: float) -> float:
        """
            takes num1 and num2 and returns their difference (num1 - num2)
            num1 and num2 are numbers with decimal points
            the return value is a number with decimals (a float)
        """
        return num1 - num2
    
    @staticmethod
    def multiplication(num1: float, num2: float) -> float:
        """
            takes num1 and num2 and returns their product (num1 * num2)
            num1 and num2 are numbers with decimal points
            the return value is a number with decimals (a float)
        """
        return num1 * num2
    
    @staticmethod
    def division(num1: float, num2: float) -> float:
        """
            takes num1 and num2 and returns their quotient (num1 / num2)
            num1 and num2 are numbers with decimal points

            **IMPORTANT: before we divide, we need to check if num2 is not zero
                because we can't divide by zero, this will cause an error
            
            So, if 'num2' is zero, we raise a 'ValueError', which is a way of telling the program, 
                "Stop! You can't do this."
            Example: if we call division(10.0, 2.0), it will return 5.0 (a float).
            But if we call division(10.0, 0.0), it will raise a ValueError 
                and say "Division by zero is not allowed."
        """

        #LBYL
        if num2 == 0:
            # This part checks if 'num2' is zero. If it is, we raise an error and stop the method.
            raise ValueError("Division by zero is not allowed.")  # This sends an error message when someone tries to divide by zero.
        return num1 / num2  # If 'num2' is not zero, we divide the first number (num1) by the second number (num2) and return the result.
       
    
