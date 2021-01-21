""" 

Purpose
-------
Introduction to Exception Handling in Python.

Summary
-------
Exception Handling is used to handle error when a code does not go as planned. 
You can give a more specific error message depending on the type of error. 

Structure of Exception Handling:
-------------------------------
try:                 
    <code to execute>  #Operation code that could potentially raise an exception.
except:
    <code to execute>  #When an error occurs in try block, print errors and useful messages only. 
    <code to execute>  #If no errors in try block then except block is skipped. 
    <code to execute>  #Can have multiple except blocks. Specific errors is first then generic errors at the bottom.
else:
    <code to execute>  #If no error in try block, the else block is executed. 
finally: 
    <code to excute>   #The code in this block is excuted no matter what happens in try, except, or else block. 

"""

#Uncomment to run examples below. 
"""
#Example 1: Division by zero error with no error handling.
#Prints a trace back with error "ZeroDivisionError: division by zero".
my_num = 10
division = 10 / 0 
"""

"""
#Example 2: Division by zero error with generic error handling.
#Prints "Generic error, not sure what happened".
#This example catches all exception and it is very generic. 
my_num = 10
try:
    division = my_num / 0
except:
    print("Generic error, not sure what happened")
"""

"""
#Example 3: Division by zero  error with spefific error handling.
#Prints "Error: the number cannot be divided by 0!"
my_num = 10 
try:
    division = my_num / 0
except ZeroDivisionError:
    print("Error: the number cannot be divided by 0!")
"""

"""
#Example 4: Division by zero error and type error.
#Prints "Error: the value input in my_num should be an integer or float."
#TypeError in the first except block was executed, ZeroDivisionError except block is skipped. 
#It only runs an except block if the error matches and ignores the rest of except blocks just like if conditions. 
my_num = "a"
try: 
    division = my_num / 0
except TypeError:           
    print("Error: the value input in my_num should be an integer or float.") 
except ZeroDivisionError:
    print("Error: the number cannot be divided by 0!")
"""

"""
#Example 5: Working division example, and else statement
#Prints "This block will execute if try block has no errors."
#The else block is executed when there are no errors in the try block, otherwise, is skipped. 
my_num = 4
try: 
    division = my_num / 2
except TypeError:           
    print("Error: the value input in my_num should be an integer or float.") 
except ZeroDivisionError:
    print("Error: the number cannot be divided by 0!")
else:
    print("This block will execute if try block has no errors.")
"""

"""
#Example 6: Working division example, else statement, and finally statement.
#Prints "This block will execute if try block has no errors" and "This block will execute no matter if there are exceptions or not."
#The finally block will execute no matter if there are exceptions or not. 
my_num = 4
try: 
    division = my_num / 2
except TypeError:           
    print("Error: the value input in my_num should be an integer or float.") 
except ZeroDivisionError:
    print("Error: the number cannot be divided by 0!")
else:
    print("This block will execute if try block has no errors.")
finally: 
    print("This block will execute no matter if there are exceptions or not.")
"""

"""
#Example 7: Division by zero error, type error, else statement, finally statement. 
#Prints "This block will execute if try block has no errors." and "This block will execute no matter if there are exceptions or not."
my_num = 1
try: 
    division = my_num / 0
except TypeError:           
    print("Error: the value input in my_num should be an integer or float.") 
except ZeroDivisionError:
    print("Error: the number cannot be divided by 0!")
else:
    print("This block will execute if try block has no errors.")
finally: 
    print("This block will execute no matter if there are exceptions or not.")
"""