#Task 1 - String Slicing and Indexing
task1 = "Python is amazing!"
print(f"First word:",task1[0:6])
print(f"Amazing part:",task1[10:17])
print(f"Reversed strig:",task1[::-1])

#Task 2 - String Methods
task2 = " hello, python world! "
print(task2.strip())
print(task2.capitalize())
print(task2.replace("world","universe"))
print(task2.upper())


#Task 3 - Check for Palindromes

word = input("Enter a word:")
if word  == word[::-1]:
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"Sorry, '{word}' is not a palindrome!")