#Loops
"""
For loop
While loop
Nested loop
"""

#for loop

for i in range(5):
    #print(f"Works: ",i)
    print(i**2)


#While Loop - Repetitive worker

i = 0
while i<5:
    print("I'm a programmer",i)
    if(i==1):
        print("You need practice")
    if(i==3):
        break
    i+=1

#use continue cautiously

#Nested Loops :
# Outer loop:
#   inner loop:

for x in range(1,3):
    for y in range(2):
        print(f"i={x}, j={y}", end="\n")
    print(f"You can do it !!!") 
 

 #while nested loop
i=0
while i<5:
    j=0 
    print(f"while nested:{i}")
    while j<4:
        print(f"i= {i},j={j}")
        j+=1
    i+=1


#mix while and for loop
for k in range(1,2):
    j=0
    while j<3:
        print(f"for i{k}, while {j}")
        j+=1

x = 0
while x < 5:
            print(x) 
            x += 1

for i in range(3):
         print(i)

for i in range(5):

    if i == 3:

        break

    print(i)


for num in range(10, 16):

    if num % 3 == 0:

        continue

    if num == 14:

        break

    print(num, end=" ")