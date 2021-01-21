"""

Purpose
-------
Introduction to functions. 

Summary
-------
A function is a block of organised, reusable code that is used to perform a single or related action.
A function block is executed when called. 

Structure of function block
---------------------------
def <func_name>(<optiona_params):
    <execute code> 
    <optional return value(s)>

"""

#Uncomment to see each example. 

"""
#Example 1: Simple addition function with no parameters and returns no value. 
#Prints "The total sum is 4."
#The function wil only execute when called. 
def addition():
    sum = 2 + 2 
    print("The total sum is " + str(sum) + ".")
addition()
"""

"""
#Example 2: Simple addition function with 2 parameters and returns no value. 
#Prints "The total sum is 9."
#You will need to pass in 2 numbers when calling the function, or else it will throw an error. 
def addition(num_1, num_2):
    sum = num_1 + num_2
    print("The total sum is " + str(sum) + ".")
addition(3, 6)
"""

"""
#Example 3: Simple addition function with 2 parameters and returning a value 
#Prints "The total sum is 9." and "My calculation is 9."
#The function returns a value which is stored in variable my_calculation. 
def addition(num_1, num_2):
    sum = num_1 + num_2
    print("The total sum is " + str(sum) + ".")
    return sum
my_calculation = addition(3, 6)
print("My calculation is " + str(my_calculation) + ".")
"""

"""
#Example 4: Simple addition function with 2 parameters and returning 2 values. 
#Prints the following: 
    #"The total sum_1 is 4."
    #"The total sum_2 is 7."
    #"My calculation 1 is 4."
    #"My calculation 2 is 7."
#The value returned is a tuple where each individual values in the tuple is stored in my_calculation_1 and y_calculation_2 variable.
def addition(num_1, num_2):
    sum_1 = num_1 + 1
    sum_2 = num_2 + 1
    print("The total sum_1 is " + str(sum_1) + ".")
    print("The total sum_2 is " + str(sum_2) + ".")
    return sum_1, sum_2
my_calculation_1, my_calculation_2 = addition(3, 6)
print("My calculation 1 is " + str(my_calculation_1) + ".")
print("My calculation 2 is " + str(my_calculation_2) + ".")
"""

"""
#Example 5: Simple addition with 2 parameters default and returning 2 values. 
#Prints:
    #The total sum_1 is 2.
    #The total sum_2 is 3.
    #My calculation 1 is 2.
    #My calculation 2 is 3.
#The function is called without passing any parameters and the default parameter values are being used. 
def addition(num_1 = 1, num_2 = 2):
    sum_1 = num_1 + 1
    sum_2 = num_2 + 1
    print("The total sum_1 is " + str(sum_1) + ".")
    print("The total sum_2 is " + str(sum_2) + ".")
    return sum_1, sum_2
my_calculation_1, my_calculation_2 = addition()   
print("My calculation 1 is " + str(my_calculation_1) + ".")
print("My calculation 2 is " + str(my_calculation_2) + ".")
"""

"""
#Example 6: Variable scopes. 
#Prints "hello world" and throws NameError because it cannot find num_1 when num_1 is being printed outside of the function.
#The sentence variable is a global variable and can be accessed inside the function.
#Any variable instantiated inside the function cannot be accessed outside of the function. 
sentence = "hello world"
def addition(num_1, num_2):
    sum = num_1 + num_2
    print(sentence)
    return sum
#This would not work. 
my_calculation = addition(1, 2)
print(num_1)
"""