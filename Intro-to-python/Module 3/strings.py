# Strings can be included inside ',","""
#Slicing

StringVal = "Hello,Python"
print(StringVal[0:5])
"""
lower()
upper()
strip()
replace()
split()
join()

"""

# help(str)- This gives methods avilable

name = input("Enter your full name")
result = len(name)
spacePosition = name.find(" ")
print(result)
print(name.upper(),name.lower(), name.capitalize())
random_number = "12345-867-797979"
print(random_number[0])
print(random_number[5:]) # 5 to till the end

print(random_number[-2]) # printing from reverse position


# replace(), lstrip(), rstrip(), strip(), title()

"""
\n: New line
\t: Tab
\\: Backslash
\' or \": Single or double quotes
"""

for char in "Python":
    print(char)
for index, char in enumerate("Python"):
    print(index, char)
#String comparison in python 
print("apple" < "banana")

s = "Python"
print(s[::-1])


s = "Hello, World!"

print(s[7:12])


s = "Python"

print(s * 3)
