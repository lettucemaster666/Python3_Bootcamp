"""

Purpose 
-------
Introduction to List. 

Summary 
-------
A list is an ordered collection of items that allow each use of a set of data. 
The items can be any data types such as int, float, string, list, dictionary, or tuple.

Structure of a List
-------------------
list = [] where items are stored in between [] and each item is separated by a comma (,). 

Useful List methods
-------------------
[+] zip(): aggregates data from two list into a pair. The aggregated data can be converted to a list, dict, or tuple. 
[+] len(): counts the total number of items in a list and returns an int. 
[+] count(): counts the number of matching item found in a list. 
[+] append(): adds an item to the end of a list.
[+] sort(): will sort items in a list in order, modifies original list, and returns no value. 
[+] sorted(): will sort items in a list in order, does not modify original list, returns the sorted list. 

List manipulation Techniques
----------------------------
Structure of indexing:
[x:y:z] - x is the starting position, y is the ending position, z is the pattern of increase or decrease.

[+] [0]: accesses the first item in a list. 
[+] [1]: accesses the second item in a list
[+] [-1]: accesses the last item in a list.
[+] [-2]: accesses the second last time in a list. 
[+] [:4]: accesses the first 4 items in a list, excluding the item indexed at 4 position. i.e only 0, 1, 2, 3 index position. 
[+] [2:]: accesses the third item until the last item in a list.
[+] [:-4]: accesses every items except the last four items in a list. 
[+] [-2:]: accesses the last two items in a list.  
[+] [:10:2]: accesses even items in a list. i.e only every second item is accessed in a list. 
[+] [10::-1]: reverses the list arrangement. 

"""

"""
#Example 1: Instantiating a list of any data types. 
#Prints "[1, 2.2, 'hello world', ['I am another list', 10], {'key_1': 123, 'key_2': 456}, (69, 420)]"
my_list = [1, 2.2, "hello world", ["I am another list", 10], {"key_1": 123, "key_2": 456}, (69, 420)]
print(my_list)
"""

"""
#Example 2: Adding two lists together.
#Prints "['one', 'two', 'three', 'four', 'five', 'six']".
#Addition lists will result in combining lists together. 
list_one = ["one", "two", "three"]
list_two = ["four", "five", "six"]
list_add = list_one + list_two
print(list_add)
"""

"""
#Example 3: Accessing list items with index
#Prints:
    #"0"
    #"1"
    #"10"
    #"9"
    #"[0, 1, 2, 3]"
    #"[2, 3, 4, 5, 6, 7, 8, 9, 10]"
    #"[0, 2, 4, 6, 8]"
    #"[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]"
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[0])       #prints first item in the list 
print(my_list[1])       #prints second item in the list
print(my_list[-1])      #prints last item in the list
print(my_list[-2])      #prints second last item in the list
print(my_list[:4])      #prints the first four item in the list 
print(my_list[2:])      #prints from third to last items in the list 
print(my_list[:10:2])   #prints even items in the list excluding 10 
print(my_list[10::-1])  #prints reversed list 
"""

"""
#Example 4: zip() aggregates data from two list into a pair. The aggregated data can be converted to a list, dict, or tuple. 
#Prints: 
    #"[('Paul', 'Kito'), ('Paul', 'Kato'), ('Step', 'Meowy'), ('Jules', 'Exelsior')]"
    #"{'Paul': 'Kato', 'Step': 'Meowy', 'Jules': 'Exelsior'}"
    #"(('Paul', 'Kito'), ('Paul', 'Kato'), ('Step', 'Meowy'), ('Jules', 'Exelsior'))""
owner_names = ["Paul", "Paul", "Step", "Jules"]
catto_names = ["Kito", "Kato", "Meowy", "Exelsior"]
combinedlist_items = list(zip(owner_names, catto_names))
combineddict_items = dict(zip(owner_names, catto_names))
combinedtuple_items = tuple(zip(owner_names, catto_names))
print(combinedlist_items)
print(combineddict_items)
print(combinedtuple_items)
"""

"""
#Example 5: len() counts the total number of items in a list and returns an int. 
#Prints "11"
count_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_items = len(count_list)
print(total_items)
"""

"""
#Example 6: count() counts the number of matching item found in a list. 
#Prints
    #"2" (because there is 2 occurences of 6)
    #"1" (because there is 1 occurence of 1)
my_list = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
number_six = my_list.count(6)
number_one = my_list.count(1)
print(number_six)
print(number_one)
"""

"""
#Example 7: append() adds an item to the end of a list.
#Prints "[0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11]"
my_list = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
my_list.append(11) # Modifies existing list
print(my_list)
"""

"""
#Example 8: sort() will sort items in a list in order, modifies original list, and returns no value. 
#Numbers are sorted in ascending order. 
#Strings are sorted in alphabetical order. 
#Prints:
    #"[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
    #"['kato', 'kito', 'meow', 'tacocat', 'zebra']""
my_numlist = [10, 1, 7, 8, 4, 5, 6, 2, 3, 9, 0]
my_stringlist = ["meow", "kito", "kato", "zebra", "tacocat"]
my_numlist.sort()
my_stringlist.sort()
print(my_numlist)
print(my_stringlist)
"""

"""
#Example 9: sorted() will sort items in a list in order, does not modify original list, returns the sorted list. 
#Prints
    #"[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
    #"['kato', 'kito', 'meow', 'tacocat', 'zebra']"
my_numlist = [10, 1, 7, 8, 4, 5, 6, 2, 3, 9, 0]
my_stringlist = ["meow", "kito", "kato", "zebra", "tacocat"]
my_sorted_numlist = sorted(my_numlist)
my_sorted_stringlist = sorted(my_stringlist)
print(my_sorted_numlist)
print(my_sorted_stringlist)
"""