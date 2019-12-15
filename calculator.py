first_number = input("Type a number: ")
operator = input("Type the operation: ")
second_number = input("Type the other number: ")
expression = first_number + " " + operator + " " + second_number + " = "

if operator =="+":
     print( expression + str(int(first_number) + int(second_number)))
elif operator == "-":
    print(expression + str(int(first_number) - int(second_number)))
elif operator == "*":
    print(expression + str(int(first_number) * int(second_number)))
elif operator == "/":
    print(expression + str(int(first_number) / int(second_number)))