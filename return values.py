#defining a function which calculates area of rectangle 
def area():
    length = float(input("what is the length of a rectangle?"))
    width = float(input("what is the width of the rectangle?"))
    #returning the area of the rectangle to the main function 
    return length * width 

#defining main function to call the area() function and print the area of rectangle 
def main():
    print("the area of the rectangle is,", round(area(), 2))

main()
