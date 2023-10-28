# Test 1

"""
What is returned by the following and can you give an explanation why?
x = [1,2];
y = x
x[0]=3 
print(y == [1,2])

Edit the above code to return true.

"""

# Solution

# Printing the answer
def find_true(): # creating a function to find and print the results.
    st = input("Start the Test.. (Y)/(N) ")
    if st.lower() == "y": # condition to print steps
        print("x = [1,2]")
        print("y = x")
        print("x[0] = 3")
        print("y == [1,2] => will return False")
        print("\n")
        print("'y' is assigned with 'x' variable which holds a list so if any changes made in x will be stored/reflected in y as well (though the memory location will be different.)","If we want to change the return value to True then we need do as following", sep='\n')
        print("\n")
        print("y = list(x) => this will create a new list from x; so if any changes made in x will not affect y(It'll hold different value).")
        print("\n")
        print("hence, print(y==[1,2]) will return True!")
    else:
        print(f"Oops! wrong input: {st.upper()}")
        find_true() # calling the function


find_true()