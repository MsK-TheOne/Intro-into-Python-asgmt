message = "Welcome to the Basic Calculator Program!" 
print(message)

num1 = int(input("Enter a number: "))
operator = input("Enter an Operator (+, -, *, /): ")
num2 = int(input("Enter another number: "))
op = operator

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Cannot divide by zero."
else:
    result = "Invalid operator!"


print("Result:", num1, op, num2, "=", result)




