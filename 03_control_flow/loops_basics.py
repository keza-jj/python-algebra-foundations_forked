"""
Module 3: Control Flow for Algebraists
Learning loops and conditional logic for mathematical algorithms
"""

print("=== CONTROL FLOW: LOOPS AND LOGIC FOR ALGEBRA ===")

# 1. FOR LOOPS - Repeating mathematical operations
print("\n--- 1. For Loops - Repeating Operations ---")

print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"  Number: {i}")

print("\nFirst 5 square numbers:")
for i in range(1, 6):
    square = i ** 2
    print(f"  {i}² = {square}")

# 2. WHILE LOOPS - Repeating until condition is met
print("\n--- 2. While Loops - Conditional Repetition ---")

print("Countdown from 5:")
count = 5
while count > 0:
    print(f"  {count}...")
    count -= 1
print("  Blastoff! 🚀")

# 3. CONDITIONAL LOGIC (if/elif/else)
print("\n--- 3. Conditional Logic - Mathematical Decisions ---")

def check_number_properties(number):
    """Check various mathematical properties of a number"""
    print(f"\nAnalyzing number: {number}")
    
    if number > 0:
        print("  - Positive number")
    elif number < 0:
        print("  - Negative number")
    else:
        print("  - Zero")
    
    if number % 2 == 0:
        print("  - Even number")
    else:
        print("  - Odd number")
    
    if number > 1:
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print("  - Prime number")
        else:
            print("  - Composite number")

# Test number properties
check_number_properties(7)
check_number_properties(12)
check_number_properties(-3)

# 4. PRACTICAL ALGEBRAIC EXAMPLE: SUMMATION
print("\n--- 4. Practical Algebra: Summation ---")

def sum_first_n_numbers(n):
    """Calculate sum of first n natural numbers: 1 + 2 + 3 + ... + n"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Compare with mathematical formula: n(n+1)/2
n = 10
loop_sum = sum_first_n_numbers(n)
formula_sum = n * (n + 1) // 2

print(f"Sum of first {n} numbers:")
print(f"  Using loop: {loop_sum}")
print(f"  Using formula: {formula_sum}")
print(f"  Match: {loop_sum == formula_sum}")

# 5. BREAK AND CONTINUE
print("\n--- 5. Break and Continue - Loop Control ---")

print("Finding first prime number greater than 20:")
number = 21
while True:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"  First prime > 20: {number}")
        break
    else:
        number += 1

print("\nEven numbers from 1 to 10 (using continue):")
for i in range(1, 11):
    if i % 2 != 0:  # Skip odd numbers
        continue
    print(f"  {i}")

print("\n✅ Control flow basics complete! Ready for advanced algorithms.")