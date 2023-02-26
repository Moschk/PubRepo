number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 < number2:
    if number2 < number3:
        print(number3)
    else:
        print(number2)
else:
    print(number1)

print(max(number1, number2, number3))
