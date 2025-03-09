import random
number_to_guess = random.randint(1,100)
print(number_to_guess)
i=0
while i<10:
    number = int(input("Guess the number (between 1 and 100):"))
    if(number == number_to_guess):
        print(f"Congratulations! You guessed it in {i+1} attempts!")
        break
    if(i==9):
        print("Sorry you have used, all your attempts!!\n The correct number is : ",number_to_guess)

    i+=1
