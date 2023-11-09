"""
Name: Andrew Kwok
Group members (first names):
COSC-010
New Math Assignment
"""



"""
The NewMath class is a (poor) alternative to Python's math library. Your task
is to improve each of the components. For the variables (pi and e), you can
just improve the precision to four decimal places (they are currently only 
precise to one decimal place). For the function definitions, you should modify
them as described, without using any of the math library's functions.

Note that the main() function below demonstrates the use of each of the
functions (as well as pi).
"""
class NewMath:
    pi = 3.1415
    e = 2.7183
    
    def ceiling(x):
        """
        Calculates the closest integer that is greater than (or equal to) x.
        Function should work for negative numbers as well as non-negatives.

        Parameters
        ----------
        x : numeric (int or float)

        Returns
        -------
        int
            The ceiling of x
        """
        
        if x % 1 != 0:
            x = int(x) + 1
        return int(x)
    
    def floor(x):
        """
        Calculates the closest integer that is less than (or equal to) x. 
        Function should work for negative numbers as well as non-negatives.

        Parameters
        ----------
        x : numeric (int or float)

        Returns
        -------
        int
            The floor of x
        """

        return int(x)
    
    def factorial(x):
        """
        Calculates the factorial of x (assumes x is an integer)

        Parameters
        ----------
        x : int

        Returns
        -------
        int
            The factorial of x
        """
        factorial = 1
        while x > 0:
            factorial *= x
            x -= 1
        return factorial
    
    def greatestCommonDivisor(x, y):
        """
        Calculates greatest common divisor of x and y (assuming both are ints)

        Parameters
        ----------
        x : int
        y : int

        Returns
        -------
        int
            The greatest common divisor of x and y

        """
        x_factors = []
        y_factors = []
        
        i = x
        while i > 0:
            if x % i == 0:
                x_factors.append(i)
            i -= 1
        i = y
        while i > 0:
            if y % i == 0:
                y_factors.append(i)
            i -= 1
        
        x_factors.sort(reverse = True)
        for i in x_factors:
            if i in y_factors:
                return i
            
        
    def lowestCommonMultiple(x, y):
        """
        Calculates lowest common multiple of x and y (assuming both are ints)

        Parameters
        ----------
        x : int
        y : int

        Returns
        -------
        int
            The lowest common multiple of x and y

        """
        
        return (x * y)/NewMath.greatestCommonDivisor(x, y)
    
def main():
    """
    This function demonstrates the use of the NewMath functions. You do not 
    need to modify anything in this function.
    """
    num1 = eval(input("Enter the first number: "))
    num2 = eval(input("Enter the second number: "))
    
    print("Ceiling of the first number is", NewMath.ceiling(num1))
    print("Floor of the second number is", NewMath.floor(num2))
    print("Factorial of the first number is", NewMath.factorial(num1))
    print("Area of circle with radius", num2, "is", NewMath.pi *(num2 **2))
    print("The greatest common divisor of the two numbers is",
          NewMath.greatestCommonDivisor(num1, num2))
    print("The lowest common multiple of the two numbers is",
          NewMath.lowestCommonMultiple(num1, num2))
    
main()