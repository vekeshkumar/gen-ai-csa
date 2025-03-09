#Project- Shopping Cart
print(f"Welcome to the Inventory Manager!")
print("Current inventory:")

#Step -1
#Create the inventory Dictionary with some  key and values - where values are in tuples format
inventory ={
"apple": (10, 2.5),
"banana": (20, 1.2),
"orange":(45,2.3)
}

#Loop through the each entry in the dictionary to print the items in the inventory dictionary
for item,value in enumerate(inventory.items()):
    print("Item: ",item," Quantity: ",value[0], " Price: $", value[1])
#Step -2 Add, Remove, Update Items - Updated inventory with new value
inventory.update({"mango":(15,3.0)})
print("Adding a new item:",list(inventory.keys())[-1])
#Deleted the inventory item - Orange
del inventory["orange"]
#Update the Price and Quantity of Apple
inventory["apple"] = (5,2.5)

#Step 3: Display the Inventory
print(f"Update inventory:")
for item,value in enumerate(inventory.items()):
     print("Item: ",item," Quantity: ",value[0], " Price: $", value[1])

#Step 4: Bonus - Calculate Total Value
totalVal = 0.0
for value in inventory.values():
    totalVal+=value[1]
print(f"Total value of inventory: ${totalVal}")