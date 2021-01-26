""" 

Purpose
-------
Introduction to loops. 


Summary 
-------
Loops are used to iterage over a sequence (either a list, tuple, dictionary, or a string).

Structure of Loop
-----------------
For loop:
for <x> in <x-range>:
    <execute code> 

While loop:
while <x>:   #where x remains true will continue executing the loop until it changes to false. 
    <execute code>  

List comprehension: 
#Provides a concise way for creating list. 
#Expression can be any kind of object go into a list. 
#A list comprehension always returns a list. 
list_comp = [expression for <item> in <list> <if conditional>]

Others
------
The following keyword can be use in a loop to perform certain actions: 
[+] break keyword: this will cause the loop to completely stop and the code following break will be ignored. 
[+] continue keyword: this will cause the loop to skip the remaining code inside the loop and begin the next iteration. 

The following function is commonly used in loop:
[+] range(<start>, <stop>, <step>): function can be used to create a list that can be used to specify the number of iterator in a loop. 

Special way of creating list:
[+] List comprehension = 
"""

#Uncomment to run each example. 
"""
#Example 1: basic For loop to iterate over number list.
#Prints: 
    #"0"
    #"1"
    #"2"
    #"3"
my_numbers = [0, 1, 2, 3]
for number in my_numbers:
    print(number)
"""

"""
#Example 2: basic While loop to iterate over number list. 
#Prints: 
    #"0"
    #"1"
    #"2"
    #"3"
my_numbers = [0, 1, 2, 3]
iterator = 0 
while iterator < len(my_numbers): 
    print(my_numbers[iterator])
    iterator +=1
"""

"""
#Example 3: utilising break in a for loop to stop the loop when a negative number is found.  
#The purpose of break is to stop a loop from continuing iterating. 
#Prints: 
    #"0"
    #"1"
    #"2"
    #"Negative number -1 is found!" #See how number 3 is not printed after the negative number?
my_numbers = [0, 1, 2, -1, 3]
for number in my_numbers:
    if number < 0:
        print("Negative number " + str(number) + " is found!")
        break
    print(number)
"""

"""
#Example 4: utilising break in a while loop to stop the loop when a negative number is found. 
#Prints: 
    #"0"
    #"1"
    #"2"
    #"Negative number -1 is found!" #See how number 3 is not printed after the negative number?
my_numbers = [0, 1, 2, -1, 3]
iterator = 0 
while iterator < len(my_numbers): 
    if my_numbers[iterator] < 0: 
        print("Negative number " + str(my_numbers[iterator]) + " is found!")
        break
    print(my_numbers[iterator])
    iterator +=1
"""

"""
#Example 5: utilising continue in a for loop to ignore negative numbers in a list and print out positive ones. 
#Prints: 
    #"0"
    #"1"
    #"2"
    #"3"
my_numbers = [0, 1, 2, -1, -2, -3, -5, 3]
for number in my_numbers:
    if number < 0:
        continue
    print(number)
"""

"""
#Example 6: utlising continue in a while loop to ignore negative numbers in a list and print out positive ones. 
my_numbers = [0, 1, 2, -1, -2, -3, -5, 3]
iterator = 0 
while iterator < len(my_numbers): 
    if my_numbers[iterator] < 0: 
        iterator +=1
        continue
    else:
        print(my_numbers[iterator])
        iterator +=1
"""

"""
#Example 6: range() function used in for loop. 
#Prints: 
    #"0"
    #"1"
    #"2"
for number in range(3):
    print(number)
print("-------------------")
#Prints:
    #"0"
    #"1"
    #"2"
    #"3"   
    #"4"
for number in range(0, 5):
    print(number)
print("-------------------")
#Prints: 
    #"0"
    #"2"
    #"4"
for number in range(0, 5, 2):
    print(number)
print("-------------------")
#Prints:     
    #"5"
    #"4"
    #"3"
    #"2"
    #"1"
for number in range(5, 0, -1): #Prints number in decending order
    print(number)
"""

"""
#Example 7: range() function used in while loop. 
#Prints: 
    #"0"
    #"1"
    #"2"
iterator = 0
range_numbers = range(3)
while iterator < len(range_numbers): 
    print(range_numbers[iterator])
    iterator +=1
print("-------------------")
#Prints:
    #"0"
    #"1"
    #"2"
    #"3"
    #"4"
iterator = 0  
range_numbers = range(0, 5)
while iterator < len(range_numbers): 
    print(range_numbers[iterator])
    iterator +=1
print("-------------------")
#Prints:
    #"0"
    #"2"
    #"4"
iterator = 0 
range_numbers = range(0, 5, 2)
while iterator < len(range_numbers): 
    print(range_numbers[iterator])
    iterator +=1
print("-------------------")
#Prints: 
    #"5"
    #"4"
    #"3"
    #"2"
    #"1"
iterator = 0 
range_numbers = range(5, 0, -1)
while iterator < len(range_numbers): 
    print(range_numbers[iterator])
    iterator +=1
"""

"""
#Example 8: nested for loops. 
#Prints:
    1111111111111
    2222222222
    2222222222
    1111111111111
    2222222222
    2222222222
    1111111111111
    2222222222
    2222222222
for number_1 in range(3):
    print("1111111111111")
    for number_2 in range(2):
        print("2222222222")
"""

"""
#Example 9: list comprehension example. 
#Prints: [0, 1, 2, 3, 4]
my_list = [number for number in range(5)]
print(my_list)
"""

"""
#Example 10: list comprehension example 2. 
#Prints: [0, 2, 4, 6, 8]
my_list = [number * 2 for number in range(5)]
print(my_list)
"""
