# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")

## result = int(num1) + int(num2)
# result = float(num1) + float(num2)

# print(result)

# Calculator 2 

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")
