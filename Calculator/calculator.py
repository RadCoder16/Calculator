# Simple calculator 

num = float(input("Enter a number: "))
op = input("Enter a operator: ")
num2 = float(input("Enter another number: "))


if op == "+":
    print(num + num)
elif op == "-":
    print(num - num2)
elif op == "/":
    print(num / num2)
elif op == "*":
    print(num * num2)
elif op == "%":
    print(num % num2)
else:
    print("Invalid operator!")
