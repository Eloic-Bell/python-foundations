x = float(input("what is the first number?"))
y= float (input("what is the second number?"))
z = input("choose a mathematical operation: + - * /")
if z == "+":
    print (f"{x + y:.2f}")
elif z == "-": 
    print(f"{x - y:.2f}")
elif z == "*":
    print (f"{x * y:.2f}")
elif z == "/":
    print(f"{x / y:.2f}")
else:
    print("please enter a valid operation")