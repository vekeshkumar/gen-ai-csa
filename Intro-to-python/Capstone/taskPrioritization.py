#User Story 1: Task Prioritization 

# Create a priority Schedule - use severity or importance count
#User Story 2: Performance Tracking 

#Phase 1: Task Management  

#Phase 2: Performance Tracking  

#Phase 3: Error Handling  
#Log the error in the file


#Import a csv file with list of scores  for different subjects 
"""
Cumulative tests
and write conditions to reason out what is feedback 
good average >90, 80 to 90, 60 to 80, 50 to 60, less than 50"""


import heapq
from datetime import datetime, timedelta

class Task:
    def __init__(self, name, deadline, priority):
        self.name = name
        self.deadline = deadline
        self.priority = priority

    def __lt__(self, other):
        return (self.priority, self.deadline) < (other.priority, other.deadline)

class Subject:
    def __init__(self, name):
        self.name = name
        self.scores = []
        self.cumulative_score = 0

    def add_score(self, score):
        self.scores.append(score)
        self.cumulative_score = sum(self.scores)

    def average_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

class StudentManager:
    def __init__(self):
        self.tasks = []
        self.subjects = {}

    def add_task(self, name, deadline, priority):
        try:
            deadline = datetime.strptime(deadline, "%Y-%m-%d")
            priority = int(priority)
            task = Task(name, deadline, priority)
            heapq.heappush(self.tasks, task)
            print(f"Task '{name}' added successfully.")
        except ValueError:
            print("Invalid input. Please use YYYY-MM-DD for deadline and a number for priority.")

    def get_next_task(self):
        if self.tasks:
            task = heapq.heappop(self.tasks)
            return f"Next task: {task.name} (Deadline: {task.deadline.strftime('%Y-%m-%d')}, Priority: {task.priority})"
        return "No tasks available."

    def add_subject(self, name):
        if name not in self.subjects:
            self.subjects[name] = Subject(name)
            print(f"Subject '{name}' added successfully.")
        else:
            print(f"Subject '{name}' already exists.")

    def add_score(self, subject_name, score):
        if subject_name in self.subjects:
            try:
                score = float(score)
                self.subjects[subject_name].add_score(score)
                print(f"Score {score} added to {subject_name}.")
                print(self.get_feedback(subject_name))
            except ValueError:
                print("Invalid score. Please enter a number.")
        else:
            print(f"Subject '{subject_name}' not found.")

    def get_subject_average(self, subject_name):
        if subject_name in self.subjects:
            avg = self.subjects[subject_name].average_score()
            return f"Average score for {subject_name}: {avg:.2f}"
        return f"Subject '{subject_name}' not found."

    def get_cumulative_score(self, subject_name):
        if subject_name in self.subjects:
            cumulative = self.subjects[subject_name].cumulative_score
            return f"Cumulative score for {subject_name}: {cumulative:.2f}"
        return f"Subject '{subject_name}' not found."

    def get_feedback(self, subject_name):
        if subject_name in self.subjects:
            avg = self.subjects[subject_name].average_score()
            if avg > 90:
                return "Excellent performance! Keep up the great work."
            elif 80 <= avg < 90:
                return "Very good performance. You're on the right track."
            elif 60 <= avg < 80:
                return "Good performance. There's room for improvement."
            elif 50 <= avg < 60:
                return "Fair performance. Focus on weak areas to improve."
            else:
                return "Needs improvement. Consider seeking additional help."
        return f"Subject '{subject_name}' not found."

    def identify_weak_areas(self):
        weak_areas = sorted(self.subjects.items(), key=lambda x: x[1].average_score())
        return "Subjects to improve: " + ", ".join([subject.name for subject, _ in weak_areas[:3]])

def main():
    manager = StudentManager()
    
    # Sample data for testing
    manager.add_subject("Math")
    manager.add_subject("Science")
    manager.add_subject("History")
    
    manager.add_score("Math", 85)
    manager.add_score("Math", 92)
    manager.add_score("Science", 78)
    manager.add_score("Science", 65)
    manager.add_score("History", 45)
    manager.add_score("History", 55)
    
    manager.add_task("Math homework", "2025-03-25", 2)
    manager.add_task("Science project", "2025-03-22", 1)
    manager.add_task("History essay", "2025-03-28", 3)
    
    while True:
        print("\n1. Add Task")
        print("2. Get Next Task")
        print("3. Add Subject")
        print("4. Add Score")
        print("5. Get Subject Average")
        print("6. Get Cumulative Score")
        print("7. Get Feedback")
        print("8. Identify Weak Areas")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter task name: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            priority = input("Enter priority (1-5, 1 being highest): ")
            manager.add_task(name, deadline, priority)
        elif choice == '2':
            print(manager.get_next_task())
        elif choice == '3':
            name = input("Enter subject name: ")
            manager.add_subject(name)
        elif choice == '4':
            subject = input("Enter subject name: ")
            score = input("Enter score: ")
            manager.add_score(subject, score)
        elif choice == '5':
            subject = input("Enter subject name: ")
            print(manager.get_subject_average(subject))
        elif choice == '6':
            subject = input("Enter subject name: ")
            print(manager.get_cumulative_score(subject))
        elif choice == '7':
            subject = input("Enter subject name: ")
            print(manager.get_feedback(subject))
        elif choice == '8':
            print(manager.identify_weak_areas())
        elif choice == '9':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
