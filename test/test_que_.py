"""
Test cases for testing the que_2
"""

import pytest
from main.que_2 import divide_objects

def test_division():
    """Testing with valid input"""
    result = divide_objects(15,3)
    assert result==5.0


def test_zero_division():
    """Method: 1 ==> Testing for zero division excpetion"""
    
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed"):
        divide_objects(5,0)
    
        
def test_value_error():
    """Method: 2 ==> Testing for invalid input"""
    with pytest.raises(TypeError) as e:
        divide_objects("a", 3)
        assert str(e.value) == "Numbers only allowed"

