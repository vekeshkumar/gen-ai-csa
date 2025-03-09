#Python Introduction
#Task 1:
name = "Robert Johnson"
age = 45
height = 5.10
print(f"Hey there, my name",name,"! I'm",age," years old and ",height,"feet tall.")

#Task 2: Playing with Numbers - Operator
num1 = 10
num2 = 3
print(f"Hey, find this addition of these numbers num1:",num1," & ","num2:",num2," is:\t",(num1+num2))

#Task 3: The Number Checker - Conditional Statements
print("Please enter the number , what you have in your mind:")
number = int(input())
if number > 0 :
    print("This number is positive.Awesome!")
elif number < 0 :
    print("This number is negative.Better luck next time!")
elif number == 0:
    print("Zero it is. A perfect balance!")
else:
    print("It's not a number or its not good input!")

