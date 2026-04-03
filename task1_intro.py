# ===== FUNCTION THAT ASKS FOR INPUT AND RETURNS A GREETING =====
# This function will ask the user for their name and create a personalized greeting

def introduce_me():
    """
    This function asks the user for their name and returns a personalized greeting.

    Note: This function doesn't need parameters because it asks for input directly!
    """

    # input() displays a message and waits for the user to type something
    # The text the user types is stored in the name variable
    name = input("What is your name? ")

    # Create a personalized greeting using the name they gave us
    greeting = f"Hello {name}! Welcome to Python learning! 🎉"

    # Return the greeting so we can use it
    return greeting


# ===== CALLING THE FUNCTION =====
# Call the function, store the result, and print it

result = introduce_me()  # This will ask the user for their name
print(result)  # This will print the personalized greeting
