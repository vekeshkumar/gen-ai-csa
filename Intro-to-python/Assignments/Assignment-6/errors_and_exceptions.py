#Task 1 - Understanding Python Exceptions
number = int(input("Enter a number:"))
try:
    print(f"100 divided by {number} is ",float(100/number))
except ValueError:
    print(f"{number} Invalid input!")
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")


#Task 2 - Types of Exceptions

my_list = ["ram","john","salim"]
my_dict={"name":"ram","age":22,"country":"India"}

try:
    print(my_list[5])
except IndexError:
    print("IndexError occurred! List index out of range.")

try:
    print(my_dict["married"])
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

try:
    full_name =  my_dict.get("name")+int(my_dict.get("age"))
except TypeError:
    print("TypeError occurred! Unsupported operand types.")


#Task 3 - Using try...except...else...finally

try:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    result = float(num1/num2)
except ValueError:
    print(f"{num1} or {num2} Invalid input!")
except ZeroDivisionError:
    print(f"Divisor cannot be zero, Oops! You cannot divide by zero.")
else:
    print(f"The result is ",result)
finally:
    print("This block always executes.")
