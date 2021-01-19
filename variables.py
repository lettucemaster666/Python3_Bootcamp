"""

Purpose
-------
Introduction to variables. 

Data 

Summary 
-------
The formart in instantiating a Python variable is to use "<variable> = <value>".
The = sign makes <variable> to store the <value>. 
There are no type contraints on how you instantiate a variable unlike other languages. 

i.e <value> can store any variable type and its variable type can be changed anytime!

Variable types in Python:
[+] integer for whole number.  
[+] float for decimal number. 
[+] string for characters, word(s) or sentence(s).
[+] bool for booleans and its used as conditions. i.e True or False. 
[+] list for storing and manipulating elements. 
[+] dictionary for storing and manipulating elements. Each item is in key:value pair format. 
[+] tuple for storing elements. Tuple are immutablng elements inside tuple cannot be changed)


"""

#An integer can be a positive or negative whole number. 
positive_number = 1 
print(positive_number)
negative_number = -1 
print(negative_number)

#A float can be a positive or negative decimal number. 
positive_float = 1.1
print(positive_float)
negative_float = -1.1 
print(negative_float)

#A string is made up of characters(s), word(s) or sentences(s).
character = "c"
print(character)
word = "wei"
print(word)
string = "Hello World"
print(string)

#A bool can be True or False. The first letter of True, and False must be capitalised in the value. 
true = True 
false = False 

#A list can be used to store and manipulate elements.
#A syntax of  [] on the value side is used to indicate a list. 
numbers = [1, 2, 3, 4, 5] 
print(numbers)
#It can store any other variable types.
a_list = [100, 420.69, "c", "KitoKato", [1, 2, 3], {"A": 1, "B": 2, "C": 3}, (1, 2, 3)]
print(a_list)

#A dictionary is like a list but it has key:value pairs. Like list, it can be used to store and manipulate the values inside it. 
#The key cannot be modified, only the value. 
#A syntax of {} on the value side is used to indicate a dictionary.
dictionary = {"A": 1, "B":2, "C":3}
print(dictionary)
#The dictionary can store any variable types. 
dictionary_random = {"A": 1, "B": 1.1, "C": "c", "D": "meow", "E": True, "F": {1: "another dict", 2: "sugoi"}, "G": [1, 2, 3,], "H": (420, 420)}
print(dictionary_random)

#A tuple is similar to a list but immutable (values stored in the tuple cannot be changed)
#A syntax of () on the value side is used to indicate a tuple. 
tup = (1,2,3,4,5,6)
print(tup)
#The tuple can store any value types
tup_random = (100, 420.69, "c", "KitoKato", [1, 2, 3], {"A": 1, "B": 2, "C": 3}, (1, 2, 3))
print(tup_random)
