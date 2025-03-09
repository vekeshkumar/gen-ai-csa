import re
password = input("enter a password")
isPasswordStr = False


#User String functions and combine exceptions and give it 
"""
Create a function that checks 
conditions
1) length >= 8  then immediately exit with print msg
2) One Lower case , One upper Case, and one digit, one special character(@, #, $)
    check all these conditions one by one
    have each condition has one fail message and 
    append them to Result set and keep the 
    Pattern how to tell that
    ie. your password needs atleast one if all three we can loop and add and till n-1 if only one is there no loop


"""

def pwdValidator():
    
    isPasswordStr = True
    print("its good")
    return isPasswordStr

if len(password) >=8:
    pwdValidator()
    print()
else:
    print(f"Your password needs to be atleast characters!")


