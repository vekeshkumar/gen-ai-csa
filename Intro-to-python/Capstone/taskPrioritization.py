"""
Python’s data structures make task management super simple!

Lists: Great for to-do lists, like tracking tasks in order.
Dictionaries: Perfect for pairing tasks with details, like due dates or statuses.
Tuples: Handy for storing things you don’t want to change, like default settings.
Sets: Awesome for removing duplicates, like avoiding repeated meeting entries.
They’re like your personal assistant, keeping everything organized!

"""


# List : Track List in order, to do list
#Dictionaries : Task with details, (due dates or status) List of dictionaries
#TUples : default settings
#Sets : For removing duplicates


"""
Task 1 : Structure of Task 
Task id, auto generate - task details - task title, task description, task priority,

Task 2: Allow user to input 


Task 3: Generate priortized schedule based on the priority
if task priority is not given then it takes next available priority

# We can use date as well to make to consider sorting and also considering the priority

"""
#Task 1: 


def getTaskInformation():
    taskList =[]
    while True:
        print("Enter the task details")
        task = input("Task name:")
        task_desc = input("Task description")
        task_priority = int(input("Task severity"))
        task_endDate = input("Date (DD/MM/YYYY):")
        taskList.append({f"task_{task}":{"description":{task_desc},"priority":{task_priority}}})

        value = input(f"Do you want to continue (y/n):")
        if value == "n" :
            break
        else:
            continue
    print(taskList)

getTaskInformation()


