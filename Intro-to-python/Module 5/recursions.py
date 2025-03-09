#RECURSION
#Repititive Functions
def factorial(n):
    if n ==1: #Base Case
        return 1  
    else: 
        return n *factorial(n-1) #Recursive Case
    
"""
Pros and Cons of Recursion vs. Iteration

Pros:
Makes certain problems easier to solve and code, especially when the task involves nested or repetitive patterns (like tree traversals).
Leads to cleaner, more readable code for problems naturally suited to recursion.
Cons:
Recursive calls can be memory-intensive due to stack usage, especially with deep recursions.
Slower than iteration for some tasks, as each function call adds overhead.
May risk stack overflow errors if the recursion depth is too great.

"""
