
# int() turns variable into an integer
x = int(input("What is x?")) 
y = int(input ("what is y"))

# + sign allows addition
print(x+y)

#float() turns variable into a decimal number
x = float(input("what is x?"))
y = float(input("what is y?"))

#round() rounds the number to the nearest whole number
z = round(x + y)

#f("{:,}") allows for commas to be added to the number outputted
print(f"{z:,}")

# calculator for division
x = float(input("what is x?"))
y = float(input("what is y?"))

# rounds the number to 2 decimal places
z = round (x/y, 2)

#can also round to 2 decimal places using f-string (f"{z:.2f}")
print(f"{z:,}")

#defining functions for calculator
#defining main function
def main():
    x = int(input("what is x"))
    print("x squared is", square(x))

# defining function 'square()' in main function to allow for squaring of a number
def square (n):
    # pow() is a built-in function that takes in 2 arguments, the first being the number to be squared and the second being the power to which it will be raised
    #returning the value of the number squared to the main function
    return pow(n, 2)
#calling the main function to run the program
main()
