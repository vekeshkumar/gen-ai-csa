#Step 1: Menu of Recursive Functions
#Step 2: Factorial Function
#Step 3: Fibonacci Function
#Step 4: Recursive Fractal Pattern (Bonus)
#Step 5: User-Friendly Program

import sys
import turtle

def recursive_factorial(n):
    """Calculate factorial using recursion"""
    if n == 0:
        return 1
    return n * recursive_factorial(n - 1)

def recursive_fibonacci(n):
    """Calculate nth Fibonacci number using recursion"""
    if n <= 1:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def draw_fractal_tree(branch_len, t):
    """Recursively draw a fractal tree using turtle graphics"""
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        draw_fractal_tree(branch_len-15, t)
        t.left(40)
        draw_fractal_tree(branch_len-15, t)
        t.right(20)
        t.backward(branch_len)

def get_positive_input(prompt):
    """Validate positive integer input"""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main_menu():
    """Display main menu and handle user input"""
    print("\nWelcome to Recursive Artistry Program!")
    while True:
        print("\nMain Menu:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci Number")
        print("3. Draw Fractal Tree")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            num = get_positive_input("Enter a number for factorial calculation: ")
            print(f"Factorial of {num} is {recursive_factorial(num)}")
        
        elif choice == "2":
            position = get_positive_input("Enter Fibonacci position: ")
            print(f"Fibonacci number at position {position}: {recursive_fibonacci(position)}")
        
        elif choice == "3":
            screen = turtle.Screen()
            t = turtle.Turtle()
            t.left(90)
            t.up()
            t.backward(100)
            t.down()
            t.color("brown")
            draw_fractal_tree(75, t)
            screen.mainloop()
        
        elif choice == "4":
            print("Thank you for using Recursive Artistry!")
            sys.exit()
        
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main_menu()
