# Test 4

"""
Improve and debugging the following code

def getWeekDayName ():
    x = date.today()
    if ( x.getWeekDay() = 0) :
        WeekDayName='Mon'  
    elif ( x.getWeekDay() = 1) :
        WeekDayName='Tue'  
    elif ( x.getWeekDay() = 2) :
        WeekDayName='Wed'  
    elif ( x.getWeekDay() = 3) :
        WeekDayName='Thu'  
    elif ( x.getWeekDay() = 4) :
        WeekDayName='Fri'  
    elif ( x.getWeekDay() = 5) :
        WeekDayName='Sat'
    elif ( x.getWeekDay() = 6) :
        WeekDayName='Sun'
    else:
        'Err';
    return WeekDayName;

"""

# Solution
# Code has been improvised.
# Refer q_4_doc.md file for documentation



from datetime import date

def get_weekday_name()-> str: 
    """
    Returns:
    str: day of the week
    """
    try:
        # List of days in week
        weekday_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        x = date.today() 
        # print(x)
        weekday = x.weekday() # inbuilt function in datetime
        # print(weekday)

        if 0 <= weekday <= 6: # Checking the day 
            return weekday_names[weekday] 
        else:
            raise ValueError("Invalid weekday value") # Raise Exception 

    except Exception as e:
        return f"Error: {e}"


weekday_name = get_weekday_name()

print(f"Today is {weekday_name}") # printing day of the week


