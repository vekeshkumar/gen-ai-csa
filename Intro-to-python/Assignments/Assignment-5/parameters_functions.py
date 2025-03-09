#Task 1 - Writing Functions
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")

def add_numbers(no1, no2):
    return ("The sum of ", no1," and ",no2," is ", no1+no2)

greet_user("Rajesh")
print(add_numbers(5,17))


#Task 2 - Using Default Parameters
def describe_pet(pet_name:str, animal_type:str = "dog"):
    print("I have a",pet_name," named ", animal_type)

describe_pet("Buddy")
describe_pet("Whiskers","Cat")

#Task 3 - Functions with Variable Arguments
def make_sandwich(*args):
    print(f"Making a sandwich with the following ingredients: ")

#Task 4 - Understanding Recursion
def factorial_recursive(val:int):
    if val ==1: return val
    return factorial_recursive * factorial_recursive(val-1)

    print(f"Factorial of 5 is ")
def fibonacci(index:int):
    #Base Case
    # Recursive case
    print(f"The 6th Fibonacci number is ")

