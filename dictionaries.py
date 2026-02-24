# Create a dictionary
MLB_teams = {
    "Colorado": "Rockies",
    "Chicago": "White Sox",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}

# You can only use hashable Python objects as dictionary keys.
{42: "aaa", 2.78: "bbb", True: "ccc"}
types_dict = {int: 1, float: 2, bool: 3}
types_dict
types_dict[float]
types_dict[bool]

# You cannot use unhashable objects as dictionary keys, such as lists or dictionaries
{[1, 2]: "A list as a key? Hmm..."}

# you can use tuples because tuples are immutable
a_dict = {(1, 1): "a", (1, 2): "b", (2, 1): "c", (2, 2): "d"}
a_dict[(1, 1)]
a_dict[(2, 1)]

# Using the dict() constructor to create a dictionary

dict()
# from variables and strings
MLB_teams = dict(
    Colorado="Rockies",
    Chicago="White Sox",
    Boston="Red Sox",
    Minnesota="Twins",
    Milwaukee="Brewers",
    Seattle="Mariners",
)

MLB_teams

# from a list of tuples
MLB_teams = dict(
    [
        ("Colorado", "Rockies"),
        ("Chicago", "White Sox"),
        ("Boston", "Red Sox"),
        ("Minnesota", "Twins"),
        ("Milwaukee", "Brewers"),
        ("Seattle", "Mariners"),
    ]
) 
# creating a dictionary from a list of tuples
MLB_teams

places = [
    "Colorado",
    "Chicago",
    "Boston",
    "Minnesota",
    "Milwaukee",
    "Seattle",
]

teams = [
    "Rockies",
    "White Sox",
    "Red Sox",
    "Twins",
    "Brewers",
    "Mariners",
]

dict(zip(places, teams))

# Accessing Dictionary Values
MLB_teams["Minnesota"]

MLB_teams["Colorado"]

# if you try to access a key that doesn't exist, you'll get a KeyError
MLB_teams["Indianapolis"]

# dict with list values
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 35,
    "spouse": "Jane",
    "children": ["Ralph", "Betty", "Bob"],
    "pets": {"dog": "Frieda", "cat": "Sox"},
}

person["children"][0]
person["children"][2]
person["pets"]["dog"]
person["pets"]["cat"]

# Traversing Dictionaries by Keys
students = {
    "Alice": 89.5,
    "Bob": 76.0,
    "Charlie": 92.3,
    "Diana": 84.7,
    "Ethan": 88.9,
    "Fiona": 95.6,
    "George": 73.4,
    "Hannah": 81.2,
}

for student in students:
    print(student)
for student in students.keys():
    print(student)
for student in students:
    print(student, "->", students[student])

# Iterating Over Dictionary Values
MLB_teams = {
    "Colorado": "Rockies",
    "Chicago": "White Sox",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}

for team in MLB_teams.values():
    print(team)
