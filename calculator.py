expression = input("Type your math expression: ")

first_number = expression[0]
operator = expression[1]
second_number = expression[2]
expression += "="

if operator =="+":
     print( expression + str(int(first_number) + int(second_number)))
elif operator == "-":
    print(expression + str(int(first_number) - int(second_number)))
elif operator == "*":
    print(expression + str(int(first_number) * int(second_number)))
elif operator == "/":
    print(expression + str(int(first_number) / int(second_number)))