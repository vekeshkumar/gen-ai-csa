"""
Defining Functions: Learn to create functions with inputs, outputs, and documentation.
Default and Keyword Arguments: Explore how to use default values and call functions with named parameters.
Arbitrary Arguments: Master *args and **kwargs for handling flexible inputs.
Lambda Functions: Discover how to write concise, anonymous functions for quick operations.
"""
def greet():
    print("Hello, This is my Python World")

#snake_case for function eg.my_function

def greet(name):
    print("Hola,{name}!")

def add(a,b):
    return a+b

# Calling Function 
#Calling by Name
greet("Ram")

#Funcitonal Parameters
#Default Parameters
def greet(name="Guest"):
    print(f"Hellp,{name}")


#Arbitrary Arguments: Use *args for a variable number of positional 
# arguments and **kwargs for keyword arguments.
def show_items(*args):
    for item in args:
        print(item)

#Scope and Lifetime of Variables

#Local vs. Global Variables: Variables defined inside a function are local and can’t be accessed outside. 
#Use the global keyword to modify global variables within a function.    
def set_count():
    global count
count =10