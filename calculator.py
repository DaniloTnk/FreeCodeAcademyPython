expression = input("Type your math expression: ")

def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second

first_number = int(expression[0])
operator = expression[1]
second_number = int(expression[2])
expression += "="

if operator =="+":
     print( expression + str(sum(first_number, second_number)))
elif operator == "-":
    print(expression + str(subtract(first_number, second_number)))
elif operator == "*":
    print(expression + str(multiply(first_number, second_number)))
elif operator == "/":
    print(expression + str(divide(first_number, second_number)))