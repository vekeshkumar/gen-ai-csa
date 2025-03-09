#Exceptions
"""
Errors and exceptions can occur for various reasons 
(syntax, runtime, or logic).

Syntax Error
Common exceptions:
ValueError
TypeError
IndexError
KeyError
ZeroDivisionError

Exception
Try-Except Blocks
Graceful Degradation

#Value Error
int("abc")
#Type Error
"Hello"+5
#Index Error
my_list=[1,2,3]
print(my_list[5])
#Key Error
my_dict = {"name":"Alice"}
print(my_dict["age"])

#Zero Division error
result = 10/0

"""

#Exceptions - try , catch, else, finally ,raise

"""
try:
    # Code that might raise an exception
except SomeException:
    # Code to run if the exception occurs
"""
def check_positive(num):
    if num == 0:
        raise ValueError("Number must be positive!")
try:
    num = int(input("enter a number positive integer:"))
    try:
        check_positive(num)
    except ValueError as e:
        print(e)
    print(10/num)
except ValueError:
    print("The number is not valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Enter input is good, proceed for further steps!")
finally:
    print("Life is short , though these errors occur, connect with people!!")


