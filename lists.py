# Creating lists
countries = ["United States", "Canada", "Poland", "Germany", "Austria"]
countries
fruits = ['apple', 'banana', 'cherry']
fruits

digits_range = list(range(10))

digits_range
digits=list((1, 2, 3))
digits


# list comprehension
even_digits = [number for number in range(1, 10) if number % 2 == 0]

even_digits

# create an empty list and add elements to it
empty_list = []
another_empty_list = list()

empty_list

heterogeneous_list = ["pythonista", 42, 3.14, True]
# Lists and tuples can even contain objects like functions, classes, and modules
int

len

def func():
    pass

func

import math
math

my_mixed_list=[int, len, func, math]
my_mixed_tuple=(int, len, func, math)

# list or tuple don’t need to be unique, they can contain duplicate items
repeated_items_list = ["bark", "meow", "woof", "bark", "cheep", "bark"]

repeated_items_tuple = ("bark", "meow", "woof", "bark", "cheep", "bark")


# Indexing and slicing lists
words = ["foo", "bar", "baz", "qux", "quux", "corge"]
words[0]
words[2]
words[5]

words[-1]
words[-2]
words[-len(words)]
# slicing list
words[2:5]
words[-5:-2]
words[1:4]
words[-5:-2] == words[1:4]

#Lists Are Mutable
letters = ["A", "B", "c", "d"]  # A list
letters[2] = "C"
letters
letters[-1] = "D"
letters

#Tuples Are Immutable
letters = ("A", "B", "c", "d")  # A tuple
letters[2] = "C"

# Deleting items from a list
fruits = ["apple", "orange", "mango", "grape"]
del fruits[0]  # Remove apple
fruits

person = ("John Doe", 35, "Web Dev")
del person[1]  # Try to remove the age value

# Replace content of a list with another list
numbers = [1, 2, 3, 0, 0, 0, 7]
numbers[3:6] = [4, 5, 6]
numbers

numbers2 = [1, 2, 3, 7]
numbers2[3:4] = [4, 5, 6, 7]
numbers2

# Appending items to a list
a = ["a", "b"]
a.append("c")
a
a.append(["c", "d", "e"])

# .insert(index, obj)
a = ["a", "c"]
a.insert(1, "b")
a

#.remove(obj)
a = ["a", "b", "c", "d", "e"]
a.remove("b")
a
a.remove("c")
a

# .pop([index=-1])
a = ["a", "b", "c", "d", "e"]
a.pop()
a
a.pop()
a

more_fruits = fruits + ['pineapple', 'tomato', 'guava'] + ['dates', 'banana']
more_fruits

# To create a copy of a list, use the copy method. Modifying the copied list does not affect the original.
more_fruits_copy = more_fruits.copy()
more_fruits_copy


# You can also use the built-in len(), min(), max(), and sum() functions with lists and tuples:
list_of_numbers = [2, 7, 5, 4, 8]
len(list_of_numbers)
min(list_of_numbers)
max(list_of_numbers)
sum(list_of_numbers)


# Tuples
# Create a tuple
connection = ("localhost", "8080", 3, "database.db")
connection

#  To define a tuple, you don’t need the parentheses
contact = "John Doe", "john@example.com", "55-555-5555"
contact

# the parentheses are optional, to define a single-item tuple, you need to use a comma
t = (2,)
type(t)
t = (2)
type(t)

# create new tuples using the tuple() constructor
tuple(range(10))

# you can convert a list into a tuple using the tuple() constructor
tuple([1, 2, 3])

# Create an empty tuple
empty_tuple= ()
tuple(empty_tuple)

fruits_tuple = ('apple', 'cherry', 'dates')
fruits_tuple

# check no. of elements
len(fruits_tuple)

# get an element (positive index)
fruits[0]

# get an element (positive index)
fruits[0]

# check if it contains an element
'dates' in fruits

# try to change an element
fruits[0] = 'avocado'

# Tuple methods
a_tuple = 23, "hello", False, None, 23, 37, "hello"
a_tuple.count
help(a_tuple.count)