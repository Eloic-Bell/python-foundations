**Week 4: Exceptions**

**date: 19/08/2026**

**What I learnt:**
- Exceptions are errors that occur when a program is running such as entering text when python is expecting a number
- 'try:' lets you run code that might cause an error, it has to be used along side 'except' that lets you handle a specified error in a defined way instead of letting the program crash
- ValueError is useful for when a value can't be converted to another value e.g. 'hello' can't be converted to an int
- 'else' works when there aren't any errors with the program
- if you use 'pass' within a while loop it will ignore and error and return to the start of the loop
- it's better to catch specific errors rather than using a broad except term 

**Examples I wrote:**
- distances.py, uses try in a while to run code and catches ValueError and KeyError by using except
- hello.py, uses while loop, try, except and pass. Pass allows code to rerun until user inputs a valid value which doesn't result in a ValueError
- mario.py, used breakpoints for run and debug, learnt about step over and step into(step into your own defined functions)
- pace.py, uses 'raise' to create conditions that would cause the program to crash


**Problems I encountered**
- remembering to use break inside of try or except to come out of the while loop 



