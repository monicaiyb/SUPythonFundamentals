# Variables and Data Types
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
# this line is tricky; try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")


# Data Types
# Numbers

2 + 2

50 - 5*6

(50 - 5*6) / 4

8 / 5  # division always returns a floating-point number 

# The integer numbers (e.g. 2, 4, 20) have type int,
#  the ones with a fractional part (e.g. 5.0, 1.6) have type float.


#Division (/) always returns a float.
17 / 3  # classic division returns a float


17 // 3  # floor division discards the fractional part

17 % 3  # the % operator returns the remainder of the division

5 * 3 + 2  # floored quotient * divisor + remainder

# the ** operator is used to calculate powers
5 ** 2  # 5 squared

2 ** 7  # 2 to the power of 7


# Strings
f"my name is {my_name}"
f"I am {my_age} years old"


types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y) 

print(f"I said: {x}")
print(f"I also said: '{y}'")


# They can be enclosed in single quotes ('...') or double quotes ("...") with the same result 
'spam eggs'  # single quotes

"Paris rabbit got your back :)! Yay!"  # double quotes

'1975'  # digits and numerals enclosed in quotes are also strings

# To quote a quote, we need to “escape” it, by preceding it with \. Alternatively, we can use the other type of quotation marks
'doesn\'t'  # use \' to escape the single quote...

"doesn't"  # ...or use double quotes instead

'"Yes," they said.'

"\"Yes,\" they said."
'"Yes," they said.'
'"Isn\'t," they said.'
'"Isn\'t," they said.'

# Strings can be concatenated (glued together) with the + operator, and repeated with *:
# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'

prefix = 'Py'
combined = prefix + 'thon'
print(combined)

# Two or more string literals 
# (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
'Py' 'thon'
'Python'


# This feature is particularly useful when you want to break long strings:
text = ('Put several strings within parentheses '
        'to have them joined together.')



# Strings can be indexed (subscripted), with the first character having index 0. 
# There is no separate character type; a character is simply a string of size one:
word = 'Python'

word[0]  # character in position 0

word[5]  # character in position 5


word[0:2] # characters from position 0 (included) to 2 (excluded)

word[2:5] # characters fro

print("doesn't")
print('doesn\'t')


mixedNumber= 5+90.8

print(type(mixedNumber))

addString='fish' + 'market'
print(addString,addString ) 

