#Task 1 - Working with Lists
fruits = ["banana","Guava","Jack Fruit","Mango","Apple"]
print(f"Original List:{fruits}")
fruits.append("Orange")
print(f"After adding a fruit:{fruits}")
fruits.remove("Jack Fruit")
print(f"After removing a fruit:{fruits}")
print(f"Reversed List",fruits[::-1])

#Task 2 - Exploring Dictionaries
personal_dict = {"name":"Vekesh","age":"22","city":"Montreal"}
personal_dict.update({"favourite color":"blue"})
print("\nKeys:", end="\t")
for keys in personal_dict.keys():
    print(keys,end="\t")
print(f"\nValues:",end="\t")
for values in personal_dict.values():
    print(values,end="\t")

#Task 3 - Using Tuples
fav_things = ("Pursuit of Happiness","Vetri Nichayam","Atomic Habits")
fav_things[0]="AGNI"
print(len(fav_things))