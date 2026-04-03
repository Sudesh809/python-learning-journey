# ===== SIMPLE CALCULATOR PROGRAM =====
# This program demonstrates functions that perform math operations


# ===== FUNCTION 1: ADD TWO NUMBERS =====
# This function takes two numbers and returns their sum

def add_numbers(num1, num2):
    """
    This function adds two numbers together.

    Parameters:
    - num1: The first number
    - num2: The second number

    Returns:
    - The sum of num1 and num2
    """

    # Add the two numbers together
    result = num1 + num2

    # Send the result back
    return result


# ===== FUNCTION 2: MULTIPLY TWO NUMBERS =====
# This function takes two numbers and returns their product

def multiply_numbers(num1, num2):
    """
    This function multiplies two numbers together.

    Parameters:
    - num1: The first number
    - num2: The second number

    Returns:
    - The product of num1 and num2
    """

    # Multiply the two numbers together
    result = num1 * num2

    # Send the result back
    return result


# ===== FUNCTION 3: SUBTRACT TWO NUMBERS =====
# This function takes two numbers and returns their difference

def subtract_numbers(num1, num2):
    """
    This function multiplies two numbers together.

    Parameters:
    - num1: The first number
    - num2: The second number

    Returns:
    - The product of num1 and num2
    """

    # Multiply the two numbers together
    result = num1 - num2

    # Send the result back
    return result


# ===== CALLING THE FUNCTIONS WITH DIFFERENT NUMBERS =====
# Now we'll use our calculator functions!

# Test 1: Adding 5 and 3
print("=== ADDITION TEST ===")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Call add_numbers with the user-provided numbers
sum_result = add_numbers(num1, num2)
print(f"{num1} + {num2} = {sum_result}")  # Print the result using f-string

print("=== Subtract TEST ===")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Call add_numbers with the user-provided numbers
sum_result = subtract_numbers(num1, num2)
print(f"{num1} - {num2} = {sum_result}")  # Print the result using f-string

# Test 2: Adding 10 and 20
print("\n=== ADDITION TEST 2 ===")
sum_result2 = add_numbers(10, 20)  # Call add_numbers with 10 and 20
print(f"10 + 20 = {sum_result2}")  # Print the result

# Test 3: Multiplying 5 and 3
print("\n=== MULTIPLICATION TEST ===")
product_result = multiply_numbers(5, 3)  # Call multiply_numbers with 5 and 3
print(f"5 × 3 = {product_result}")  # Print the result

# Test 4: Multiplying 7 and 8
print("\n=== MULTIPLICATION TEST 2 ===")
product_result2 = multiply_numbers(7, 8)  # Call multiply_numbers with 7 and 8
print(f"7 × 8 = {product_result2}")  # Print the result

# Test 5: Using decimals (numbers with decimal points)
print("\n=== ADDITION WITH DECIMALS ===")
decimal_sum = add_numbers(3.5, 2.5)  # Functions work with decimals too!
print(f"3.5 + 2.5 = {decimal_sum}")  # Print the result

# Test 6: Multiplying decimals
print("\n=== MULTIPLICATION WITH DECIMALS ===")
decimal_product = multiply_numbers(2.5, 4)  # Mix integers and decimals
print(f"2.5 × 4 = {decimal_product}")  # Print the result


# ===== BONUS: CHAINING FUNCTIONS =====
# You can even use the result of one function as input to another!

print("\n=== CHAINING FUNCTIONS ===")
# First, add 5 and 3 to get 8
# Then, multiply that result by 2
first_operation = add_numbers(5, 3)  # This gives us 8
final_result = multiply_numbers(first_operation, 2)  # Now multiply 8 by 2
print(f"(5 + 3) × 2 = {final_result}")  # This should be 16
