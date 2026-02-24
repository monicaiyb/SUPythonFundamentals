# The if statement
a_number = 34
if a_number % 2 == 0:
    print("We're inside an if block")
    print('The given number {} is even.'.format(a_number))

# The else statement
a_number = 34
if a_number % 2 == 0:
    print('The given number {} is even.'.format(a_number))
else:
    print('The given number {} is odd.'.format(a_number))
# The given number 34 is even.
another_number = 33
if another_number % 2 == 0:
    print('The given number {} is even.'.format(another_number))
else:
    print('The given number {} is odd.'.format(another_number))

# The elif statement
today = 'Wednesday'
if today == 'Sunday':
    print("Today is the day of the sun.")
elif today == 'Monday':
    print("Today is the day of the moon.")
elif today == 'Tuesday':
    print("Today is the day of Tyr, the god of war.")
elif today == 'Wednesday':
    print("Today is the day of Odin, the supreme diety.")
elif today == 'Thursday':
    print("Today is the day of Thor, the god of thunder.")
elif today == 'Friday':
    print("Today is the day of Frigga, the goddess of beauty.")
elif today == 'Saturday':
    print("Today is the day of Saturn, the god of fun and feasting.")

a_number = 15
if a_number % 2 == 0:
    print('{} is divisible by 2'.format(a_number))
elif a_number % 3 == 0:
    print('{} is divisible by 3'.format(a_number))
elif a_number % 5 == 0:
    print('{} is divisible by 5'.format(a_number))
elif a_number % 7 == 0:
    print('{} is divisible by 7'.format(a_number))

# Using if, elif, and else together
a_number = 49
if a_number % 2 == 0:
    print('{} is divisible by 2'.format(a_number))
elif a_number % 3 == 0:
    print('{} is divisible by 3'.format(a_number))
elif a_number % 5 == 0:
    print('{} is divisible by 5'.format(a_number))
else:
    print('All checks failed!')
    print('{} is not divisible by 2, 3 or 5'.format(a_number))

# Nested conditional statements

a_number = 15
if a_number % 2 == 0:
    print("{} is even".format(a_number))
    if a_number % 3 == 0:
        print("{} is also divisible by 3".format(a_number))
    else:
        print("{} is not divisible by 3".format(a_number))
else:
    print("{} is odd".format(a_number))
    if a_number % 5 == 0:
        print("{} is also divisible by 5".format(a_number))
    else:
        print("{} is not divisible by 5".format(a_number))

# Ternary operator:
parity = 'even' if a_number % 2 == 0 else 'odd'
print('The number {} is {}.'.format(a_number, parity))

# The pass statement
if a_number % 2 == 0:                     #in case of even number, the condition satisfied and so no outpur in print staement. But for odd, we will get output.
    pass
elif a_number % 3 == 0:
    print('{} is divisible by 3 but not divisible by 2'.format(a_number))

# While Loops
result = 1
i = 1

while i <= 100:
    result = result * i
    i = i+1
    #print('The factorial of {} iteration is: {}'.format(i, result))                                   #this will print result of each iteration. Just uncoment it and see the results

print('The factorial of 100 is: {}'.format(result))

line = '*'
max_length = 10

while len(line) < max_length:
    print(line)
    line += "*"
    
while len(line) > 0:
    print(line)
    line = line[:-1]

# INFINITE LOOP - INTERRUPT THIS CELL
result = 1
i = 1
while i <= 100:
    result = result * i
    # forgot to increment i