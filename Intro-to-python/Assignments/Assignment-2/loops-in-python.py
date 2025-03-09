#Task-1 : Counting Down with Loops
countdown = int(input("Enter the starting number: "))
while countdown>0:
    print(countdown)
    #if(countdown==1): print("Blast off!🚀")
    countdown-=1
print("Blast off!🚀")

#Task-2 : Multiplication Table with for Loops

multiInput = int(input("Enter a number:"))
for i  in range(1,11):
    print(f"{multiInput} X {i} = ",multiInput*i)

#Task-3 : Find the Factorial
number = int(input("Enter a number:"))
cnt = 1
for i in range(1,(number+1)):
    cnt = cnt*i
print(f"The Factorial of {number} is ",cnt)