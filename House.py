name = input("what is your name?")
#match allows for multiple cases to be checked against a variable
match name:
    #case allows for a specific case to be checked against the variable 'name'
    case "Harry" | "hermione" | "Ron":
        print ("Gryffindor")
    case "Draco":
        print("Slytherin")
    #case _ allows for a default case for names that aren't mentioned in cases above
    case _:
        print("Who?")