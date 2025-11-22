"""
20 Function Challenges for Algebraists
Solve each problem by creating a function that performs the calculation.
"""

print("=== 20 ALGEBRAIC FUNCTION CHALLENGES ===")

# Challenge 1: Greeter Function
def welcome_student(name):
    """Takes a name and returns a welcome message"""
    return f"Hello, {name}! Welcome to math class."

# Challenge 2: Perimeter of a Square
def perimeter_of_square(side_length):
    """Calculate perimeter of a square: P = 4 × side"""
    return 4 * side_length

# Challenge 3: Circle Area
def area_of_circle(radius):
    """Calculate area of a circle: A = πr² (use 3.14 for pi)"""
    return 3.14 * (radius ** 2)

# Challenge 4: Triangle Area
def area_of_triangle(base, height):
    """Calculate area of a triangle: A = ½ × base × height"""
    return 0.5 * base * height

# Challenge 5: Pythagorean Theorem
def find_hypotenuse(a, b):
    """Find hypotenuse of right triangle: c = √(a² + b²)"""
    return (a**2 + b**2) ** 0.5

# Challenge 6: Simple Interest
def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest: I = P × r × t"""
    return principal * rate * time

# Challenge 7: Average of Three Numbers
def average_of_three(a, b, c):
    """Calculate average of three numbers"""
    return (a + b + c) / 3

# Challenge 8: Maximum of Two Numbers
def find_max(num1, num2):
    """Find maximum of two numbers (without using max())"""
    if num1 > num2:
        return num1
    else:
        return num2

# Challenge 9: Power Calculation
def calculate_power(base, exponent):
    """Calculate base raised to exponent: base^exponent"""
    return base ** exponent

# Challenge 10: Fraction Simplifier (Concept)
def simplify_fraction(numerator, denominator):
    """Simplify a fraction by finding GCD"""
    # Find Greatest Common Divisor
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    common_divisor = gcd(numerator, denominator)
    simple_num = numerator // common_divisor
    simple_den = denominator // common_divisor
    return simple_num, simple_den

# Challenge 11: Celsius to Fahrenheit
def celsius_to_fahrenheit(c_temp):
    """Convert Celsius to Fahrenheit: F = (C × 9/5) + 32"""
    return (c_temp * 9/5) + 32

# Challenge 12: Feet to Meters
def feet_to_meters(feet):
    """Convert feet to meters: 1 foot = 0.3048 meters"""
    return feet * 0.3048

# Challenge 13: Percentage Calculator
def find_percentage(part, whole):
    """Calculate percentage: (part/whole) × 100"""
    return (part / whole) * 100

# Challenge 14: Slope of a Line
def find_slope(x1, y1, x2, y2):
    """Calculate slope between two points: m = (y2 - y1)/(x2 - x1)"""
    return (y2 - y1) / (x2 - x1)

# Challenge 15: Distance Between Two Points
def find_distance(x1, y1, x2, y2):
    """Calculate distance between points: d = √[(x2-x1)² + (y2-y1)²]"""
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# Challenge 16: Quadratic Formula Solver
def solve_quadratic(a, b, c):
    """Solve quadratic equation: ax² + bx + c = 0"""
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2

# Challenge 17: Factorial Calculator
def factorial(n):
    """Calculate factorial: n! = n × (n-1) × ... × 1"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Challenge 18: Even Number Check
def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

# Challenge 19: Prime Number Check
def is_prime(number):
    """Check if a number is prime"""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Challenge 20: System of Equations Checker
def is_solution(x, y, eq1, eq2):
    """
    Check if (x, y) satisfies both equations
    eq1 and eq2 are tuples (a, b, c) representing ax + by = c
    """
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2
    
    satisfies_eq1 = abs((a1*x + b1*y) - c1) < 0.0001  # Account for floating point errors
    satisfies_eq2 = abs((a2*x + b2*y) - c2) < 0.0001
    
    return satisfies_eq1 and satisfies_eq2

# Test all challenges
if __name__ == "__main__":
    print("Testing all 20 challenges:\n")
    
    # Test each challenge
    print("1.", welcome_student("Alice"))
    print("2. Perimeter of square with side 5:", perimeter_of_square(5))
    print("3. Area of circle radius 7:", area_of_circle(7))
    print("4. Area of triangle base 10 height 5:", area_of_triangle(10, 5))
    print("5. Hypotenuse of triangle 3-4-5:", find_hypotenuse(3, 4))
    print("6. Simple interest on $1000 at 5% for 2 years:", calculate_simple_interest(1000, 0.05, 2))
    print("7. Average of 10, 20, 30:", average_of_three(10, 20, 30))
    print("8. Maximum of 15 and 25:", find_max(15, 25))
    print("9. 2 raised to power 8:", calculate_power(2, 8))
    print("10. Simplify fraction 8/12:", simplify_fraction(8, 12))
    print("11. 25°C to Fahrenheit:", celsius_to_fahrenheit(25))
    print("12. 10 feet to meters:", feet_to_meters(10))
    print("13. 25 out of 50 as percentage:", find_percentage(25, 50))
    print("14. Slope between (1,2) and (4,8):", find_slope(1, 2, 4, 8))
    print("15. Distance between (1,1) and (4,5):", find_distance(1, 1, 4, 5))
    print("16. Roots of x² - 5x + 6:", solve_quadratic(1, -5, 6))
    print("17. Factorial of 5:", factorial(5))
    print("18. Is 7 even?", is_even(7))
    print("19. Is 17 prime?", is_prime(17))
    
    # Test system of equations: 2x + 3y = 12 and x - y = 1
    equation1 = (2, 3, 12)  # 2x + 3y = 12
    equation2 = (1, -1, 1)  # x - y = 1
    print("20. Is (3,2) solution to system?", is_solution(3, 2, equation1, equation2))
    
    print("\n🎉 ALL 20 CHALLENGES COMPLETED! 🎉")