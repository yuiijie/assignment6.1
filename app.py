number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")
action = input("Choose action: '+' - addition, '*' - multiplication: ")


if action == '+':
    print(int(number_1) + int(number_2))
elif action == '-':
    print(int(number_1) - int(number_2))
elif action == '*':
    print(int(number_1) * int(number_2))
else:
    print('Try again')