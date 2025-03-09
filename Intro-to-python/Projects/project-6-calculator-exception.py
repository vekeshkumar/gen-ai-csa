
import logging
#Step 1: Menu of Operations
"""
    Choose an operation: 
    1. Addition 
    2. Subtraction 
    3. Multiplication
    4 .Division 
    5. Exit 
    Enter the first number: 10
    Enter the second number: 0 
    Oops! Division by zero is not allowed. 
    Choose an operation: 5 
    Goodbye!
"""
#Step 4: Logging Errors (Bonus)
def log_error_to_file(exception, fileName="error_log.txt"):
    try:
        with open(fileName,"a") as f:
            f.write(f"ERROR:root:{type(exception).__name__} occured:{exception}\n")
    except Exception as e:
        print(f"Error writing to log file:{e}")
    finally:
        f.close()


print("Welcome to the Error-Free Calculator! ")
while(True):
    print("""Choose an operation: 
        1. Addition 
        2. Subtraction 
        3. Multiplication
        4. Division 
        5. Exit """)
    
    try:
        key = int(input())
        if key == 5:
            print("Goodbye!")
            break
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        result = 0.0
    except ValueError as V:
        print("Invalid value, Enter a valid input")
        log_error_to_file(V)
    except TypeError as T:
        log_error_to_file(T)
        print("Enter valid type to perform operation")
    else:
        if key == 1:
            result = num1+num2
            print(result)
        elif key == 2:
            result = num1-num2
            print(result)

        elif key == 3:
            result = num1 * num2
            print(result)
        elif key == 4:
            try:
                result = num1 / num2
                print(result)
            except ZeroDivisionError as ZDE:
                log_error_to_file(ZDE)
                print("Oops! Division by zero is not allowed.")
