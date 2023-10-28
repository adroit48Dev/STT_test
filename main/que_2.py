# Test - 2

"""
Create a function that takes two objects, 
“x” and “y” and returns “x” divided by “y”. 
Include error checking

"""
# Solution

def divide_objects(x: int | float, y: int | float) -> float | ZeroDivisionError | TypeError:
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed")
    except TypeError:
        raise TypeError("Numbers only allowed")
       


