number1 = float(input('enter the first_number:'))
operator = input('enter an operator(+,-,*,/,%):')
number2 = float(input('enter the second number:'))
result = None

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        print("Error: Cannot divide by zero!")
elif operator == '%':
    result = number1 % number2
else:
    print("Error: Invalid operator")

if result is not None:
    print(f"The result is: {result}")