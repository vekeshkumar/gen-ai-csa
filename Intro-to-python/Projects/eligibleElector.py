#Project : Eligible Elector
age = int(input("Hey Champ, tell me how old are you? "))

limit = 18
if age.is_integer and age < 0:
    print("Oopsie, I guess you entered something wrong , can you enter your age please!")
else:
    if age >=limit:
        print("Congratulations! You are eligible to vote. Go make a difference!")
    elif age < limit:
        print("Oops! You’re not eligible yet. But hey, only ",(limit-age)," more years to go!")