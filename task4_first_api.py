# ===== AGE FINDER: YOUR FIRST API PROJECT =====
# This program makes a request to the Agify API
# It tells you the average age of people with a given name


# INSTALLATION REQUIRED:
# =====================
# Before running this, you MUST install the requests library:
#     pip install requests
#
# Only need to do this once!


# Import the requests library
# This library makes it easy to communicate with APIs
import requests


# ===== FUNCTION TO GET AGE DATA FROM API =====

def get_average_age(name):
    """
    This function makes an API request to get the average age for a name.

    Parameter:
    - name: The name to look up (string)

    Returns:
    - A dictionary with name, age, and count
    - Or None if there was an error

    How it works:
    1. Creates the API URL with the name as a parameter
    2. Makes an HTTP GET request to that URL
    3. Gets the response (data) back from the API
    4. Converts the JSON response to a Python dictionary
    5. Returns the data or an error message
    """

    try:
        # Step 1: Create the API URL
        # The URL is: https://api.agify.io?name=[the name]
        # ?name= is a query parameter - it tells the API what to search for
        api_url = f"https://api.agify.io?name={name}"

        print(f"📡 Requesting data from: {api_url}")

        # Step 2: Make the API request
        # requests.get() sends an HTTP GET request to the API
        # It waits for and receives the response
        response = requests.get(api_url)

        # Step 3: Check if the request was successful
        # response.status_code tells us if the request worked
        # 200 = success, 404 = not found, 500 = server error, etc.
        if response.status_code != 200:
            print(f"❌ Error: API returned status code {response.status_code}")
            return None

        # Step 4: Convert the response to Python data
        # response.json() converts the JSON response to a Python dictionary
        # JSON is the format the API uses to send data back to us
        data = response.json()

        # Step 5: Return the data
        return data

    # ERROR HANDLING: What if something goes wrong?
    except requests.exceptions.ConnectionError:
        # This happens if there's no internet connection or API is down
        print("❌ Error: Cannot connect to the API. Check your internet connection!")
        return None

    except requests.exceptions.Timeout:
        # This happens if the API takes too long to respond
        print("❌ Error: The API took too long to respond. Try again!")
        return None

    except requests.exceptions.RequestException as e:
        # This catches any other request-related errors
        print(f"❌ Error: Something went wrong with the request: {e}")
        return None

    except ValueError:
        # This happens if the response is not valid JSON
        print("❌ Error: API returned invalid data")
        return None


# ===== FUNCTION TO DISPLAY THE RESULTS =====

def display_results(name, data):
    """
    This function displays the results in a nice format.

    Parameter:
    - name: The name that was searched
    - data: The dictionary containing the API response
    """

    if data is None:
        print("Could not retrieve data.")
        return

    # Extract the information from the response
    average_age = data.get("age")  # Get the age (or None if not present)
    count = data.get("count")      # Get how many people in the dataset

    # Check if we got valid data
    if average_age is None or count is None:
        print("❌ Error: No data found for that name")
        return

    # Display the results nicely
    print("\n" + "=" * 50)
    print(f"📊 RESULTS FOR '{name.upper()}'")
    print("=" * 50)
    print(f"Average age: {average_age} years old")
    print(f"Based on: {count:,} people in the dataset")
    print("=" * 50 + "\n")


# ===== MAIN PROGRAM =====

def main():
    """
    This is the main function that runs the program.
    It asks the user for a name and displays the results.
    """

    print("🎯 AGIFY AGE FINDER")
    print("=" * 50)
    print("Find the average age of people with your name!")
    print("=" * 50 + "\n")

    # Ask the user for a name
    user_name = input("Enter a name (or 'quit' to exit): ").strip()

    # Allow user to quit
    if user_name.lower() == 'quit':
        print("Goodbye! 👋")
        return

    # Check if user entered something
    if not user_name:
        print("❌ Error: Please enter a valid name")
        return

    # Get the data from the API
    print()
    result = get_average_age(user_name)

    # Display the results
    display_results(user_name, result)


# ===== TESTING THE PROGRAM WITH EXAMPLES =====

if __name__ == "__main__":
    # The if __name__ == "__main__": means this only runs when you run THIS file
    # It won't run if you import this file in another program

    print("🚀 STARTING AGE FINDER PROGRAM\n")

    # Let's test with some example names first (without user input)
    print("--- EXAMPLE 1: Finding age of 'Michael' ---")
    michael_data = get_average_age("michael")
    display_results("michael", michael_data)

    print("--- EXAMPLE 2: Finding age of 'Alice' ---")
    alice_data = get_average_age("alice")
    display_results("alice", alice_data)

    print("--- EXAMPLE 3: Finding age of 'Raj' ---")
    raj_data = get_average_age("raj")
    display_results("raj", raj_data)

    print("\n" + "=" * 50)
    print("✨ NOW IT'S YOUR TURN!")
    print("=" * 50)

    # Now let the user try it
    main()


# ===== HOW THIS PROGRAM WORKS STEP-BY-STEP =====
#
# 1. Import requests library
#    → Makes API communication possible
#
# 2. User enters a name
#    → Program gets the name from the user
#
# 3. Build the API URL
#    → https://api.agify.io?name=michael
#    → The ?name= part passes the name to the API
#
# 4. Make the request
#    → requests.get(url) sends the request
#    → Waits for the API to respond
#
# 5. Get the response
#    → API sends back JSON data
#    → response.json() converts it to Python dictionary
#
# 6. Display results
#    → Shows the average age and count
#
# 7. Error handling
#    → If anything goes wrong, shows user-friendly error message
#    → Doesn't crash the program!
