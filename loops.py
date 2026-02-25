# for Statements
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# It is hard to modify a collection while iterating over it. The above code creates a copy of the dictionary and iterates over the copy, while modifying the original dictionary.
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# The range() Function
# If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy.
for i in range(5):
    print(i)

#The given end point is never part of the generated sequence; range(10) generates 10 values, 
# the legal indices for items of a sequence of length 10. 
#t is possible to let the range start at another number, or to specify a different increment
list(range(5, 10))

list(range(0, 10, 3))

list(range(-10, -100, -30))

# To iterate over the indices of a sequence, you can combine range() and len() as follows
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


# break and continue Statements
# The break statement breaks out of the innermost enclosing for or while loop:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

# The continue statement continues with the next iteration of the loop:
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")


# else Clauses on Loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else: # (Yes, this is the correct code. Look closely: the else clause belongs to the for loop, not the if statement.)
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# pass Statements
# The pass statement does nothing. 
# It can be used when a statement is required syntactically but the program requires no action
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)
    break

def initlog(*args):
    pass   # Remember to implement this!
