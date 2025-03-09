#Tuples - Immutable, fixed 
example_tuple = (1,2,"hello tupple")
single_element_tuple = (5,)
print(single_element_tuple[0])


"""

Uses of Tuples
Immutable Data Containers:
Tuples are perfect for storing data that shouldn’t be changed, like:

Coordinates (e.g., (x, y) positions).
Configuration settings.
Constant values (e.g., days of the week).
Hashable and Safe:
Because tuples are immutable, they can be used as keys in dictionaries or added to sets—something you can’t do with lists.w
"""
#Dictionaries
student = {"name":"Alex","age":21,"major":"Math"}

print(student["name"])


#use get() if you dont know the key , then it wont throw error
print(student.get("age"))

#To add in a new  key value pair
student["grade"] = "A"

#also updating existing value
student["age"] =31

#Remove stuff
del student["age"] 
#Remove a key get its value
student.pop("grade")

print(student.popitem())
#clear() wipeout  whole dictionary


# in or not in 

if "name" in student:
    print(f"{student.get("name")} is present in the dictionary!")
print(len(student))



my_list = [1, 2, 3]
my_list.append(4)
print(my_list)


my_tuple = (1, 2, 3)
print(my_tuple[1])


my_list = [1, 2, 3, 4, 5]

print(my_list[1:4])


my_dict = {"a": 1, "b": 2, "c": 3}

print(my_dict["b"])