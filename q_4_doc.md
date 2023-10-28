# get_weekday_name.py (Debugging & Improvisation) Documentation

## Code Explanation:

The code defines a function `get_weekday_name()` that returns the name(short) of the current weekday (Mon, Tue, Wed, Thu, Fri, Sat, Sun). The function utilizes the `date` class from the `datetime` module.

## Changes Made:

1. Replaced function name with underscore as per PEP8 standards.
2. Replaced `x.getWeekDay()` with `x.weekday()` to directly get the weekday index.
3. Removed the need for multiple `if-elif` statements by using the array directly.
3. Removed unnecessary semicolon (`;`) at the end of line.
4. Used an array `weekday_names` to store the names of days of the week.

## Exception Handling:

The code includes a try-except block to handle potential exceptions. If an exception occurs, the function returns an error message with details about the exception.

## Usage:

```python que_3.py```
