""" 

Purpose
--------
Introduction to Control Flow

Summary
-------
Introduces if, elif, else statements to control conditions of code.
Operators will be introduced in evaluating true or false of the control flow statements. 
 
Structure of condition statement
--------------------------------
if something_is_true: 
    execute code

if something_is_false:
    code will not executute
elif something_else_is_true:   # You can specify multiple elif statements between if and else
    code will execute
else:
    code will not execute because elif is executed 

if something_is_false:
    code will not executute
elif something_else_is_false:  # You can specify multiple elif statements between if and else
    code will not execute
else:
    code will execute

Types of operators
------------------ 
[+] or
[+] == (equal)
[+] != (not equal)
[+] and 
[+] not
[+] <, >, <=, >= (comparisons)

Other
-----
[+] in has 2 purpose: 
    1.Used to check if a value is present is a sequence (list, range, string, dictionary, etc). 
    2.Used in iterate through a sequence in a for loop. 

Exercises 
---------
Exercises for "or"
[+] True or True            #Evaluates to True 
[+] True or False           #Evaluates to True
[+] False or False          #Evaluates to False
[+] 1 < 2 or 3 < 1          #Evaluates to True
[+] 3 < 1 or 1 > 6          #Evaluates to False
[+] 1 == 1 or 1 < 2         #Evaluates to True
Exercises for "==":
[+] 1 == 1                  #Evaluates to True
[+] "hi" == "hi"            #Evaluates to True 

Exercises for "!=":
[+] 1 != 1                  #Evaluates to False 
[+] 1 != 2                  #Evaluates to True 
[+] "hi" != "ho"            #Evaluates to True

Excersises for "and":
[+] 1 == 1 and 2 > 1        #Evaluates to True
[+] 1 == 1 and 2 < 1        #Evaluates to False 
[+] "m" in "meow" and True   #Evaluates to True

Excerises for "not":
[+] "m" not in "dog"        #Evaluates to True 
[+] 2 not in [1,2,3,4]      #Evaluates to False

Excerises for "<, >, <=, >=":
[+] 3 < 2                   #Evaluates to False 
[+] 2 > 1                   #Evaluates to True
[+] 2 <= 2                  #Evaluates to True 
[+] 1 >= 0                  #Evaluates to True

"""

#Example 1: ice cream flavours
#This example prints out "My ice cream is vanilla flavoured. Creamy delicious!".
my_flavour = "vanilla"
if my_flavour == "chocolate":
    print("My ice cream is " + my_flavour + " flavoured. Yum and delicious!")
elif my_flavour == "strawberry":
    print("My ice cream is " + my_flavour + " flavoured. Reddy delicious!")
elif my_flavour == "vanilla":
    print("My ice cream is " + my_flavour + " flavoured. Creamy delicious!")
else:
    print("I will just eat the cone then")

#Example 2: simple math 
#This example prints out "0 < 2 is True".
if 0 > 2: 
    print("0 > 2 is False")
elif 0 < 2:
    print("0 < 2 is True")
else:
    print("There is no correct answer")

#Example 3: a house in neighbourhood
#This example prints "Like son like father!".
family_1 = ["father", "mother", "son", "daughter"]
if "doggo" in family_1:
    print("Who is a good boi?")
elif "son" in family_1:
    print("Like son like father!")
else:
    print("Happy fam")
