"""
Module 2: Functions for Algebraists
Learning to create reusable mathematical operations
"""

print("=== FUNCTIONS: CREATING REUSABLE MATHEMATICAL TOOLS ===")

# 1. BASIC FUNCTION SYNTAX
print("\n--- 1. Basic Function Syntax ---")

def greet_student(name):
    """A simple function that greets a student"""
    return f"Hello, {name}! Welcome to math class."

# Using the function
message = greet_student("Alice")
print(message)

# 2. MATHEMATICAL FUNCTIONS
print("\n--- 2. Mathematical Functions ---")

def calculate_area(length, width):
    """Calculate area of a rectangle"""
    area = length * width
    return area

# Using the mathematical function
room_area = calculate_area(10, 5)
print(f"Area of 10x5 rectangle: {room_area} square units")

# 3. FUNCTIONS WITH MULTIPLE PARAMETERS
print("\n--- 3. Functions with Multiple Parameters ---")

def linear_function(x, slope, intercept):
    """Calculate y = mx + b"""
    y = slope * x + intercept
    return y

# Using the linear function
y_value = linear_function(3, 2, 1)  # y = 2*3 + 1
print(f"For y = 2x + 1, when x=3: y = {y_value}")

# 4. FUNCTIONS WITH DEFAULT VALUES
print("\n--- 4. Functions with Default Values ---")

def power_function(base, exponent=2):
    """Calculate base^exponent (default exponent is 2)"""
    return base ** exponent

# Using with and without default
square = power_function(5)      # Uses default exponent=2
cube = power_function(5, 3)     # Specifies exponent=3
print(f"5² = {square}")
print(f"5³ = {cube}")

print("\n✅ Function basics complete! Ready for the 20 challenges.")