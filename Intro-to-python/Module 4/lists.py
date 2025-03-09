#Lists
my_list = [1,"apple",3.5]
my_list[0] #1
my_list[-1] #from the end- Negative indexing
my_list[0:2]
#Nested List

nested_list = [1,[2,3],4]

print(nested_list[1][1])


#Changing List ie. mutable
#add items
nested_list.append(3)
# Extend - Merge another list into yours

#insert  insert at specific position


#removing stuff

#remove()
#pop()

#clear()



#change values : just reassign using an index


fruits =["apple","banana","orange","coco"]

print(fruits[::-1])

print(dir(fruits))
for x in fruits:
    print(x)
#list sort - use help functions to get list of thing it has


#find some value present in the loops
print("apple" in fruits)
fruits[2]="pineapple"
fruits.append("orange")
fruits.reverse()

#shortcuts
squares = [x**2 for x in range(5)]

#with conditions

events = [x for x in range(10) if x%2==0]

#Nested - Perfect for 2D grids or patterns

matrix = [[i*j for j in range(3)] for i in range(3)]


#Sorting and reversing

events.sort()
events.reverse()
sorted_list =  sorted(events)
print(sorted_list)
print(events[::-1])

id = fruits.index("pineapple")
item_count = fruits.count(1)
print(item_count)
copy_fruits = fruits.copy()

print(copy_fruits)
