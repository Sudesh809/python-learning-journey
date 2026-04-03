# ===== NUMBER GUESSING GAME =====
# A fun interactive game where you try to guess the computer's number!
# This teaches: random numbers, loops, conditionals, and functions


# Import the random module (built into Python!)
# random.randint() generates random numbers
import random


# ===== FUNCTION: PLAY ONE ROUND OF THE GAME =====

def play_game():
    """
    This function runs one complete game.
    The user tries to guess a random number.

    Returns:
    - The number of attempts it took to guess correctly
    """

    # Step 1: Computer picks a random number
    # random.randint(1, 100) picks a number from 1 to 100 (inclusive)
    secret_number = random.randint(1, 100)

    # Initialize variables
    attempts = 0  # Count how many guesses the user makes
    guessed = False  # Has the user guessed correctly? (starts as False)
    previous_guesses = []  # Keep track of all previous guesses

    # Print welcome message
    print("\n" + "=" * 50)
    print("🎮 NUMBER GUESSING GAME")
    print("=" * 50)
    print("I'm thinking of a number between 1 and 100...")
    print("Can you guess it? 🤔\n")

    # Step 2: Loop until the user guesses correctly
    # "while not guessed:" means "keep looping until guessed becomes True"
    while not guessed:

        try:
            # Ask the user for their guess
            user_guess = input("🎯 Enter your guess (1-100): ")

            # Convert the text to a number
            # int() converts string "50" to number 50
            guess = int(user_guess)

            # Check if the guess is in the valid range
            if guess < 1 or guess > 100:
                print("❌ Please enter a number between 1 and 100!\n")
                continue  # Skip to the next loop without counting as an attempt

            # Add 1 to the attempt counter
            attempts += 1

            # Check if this guess was already made
            if guess in previous_guesses:
                print(
                    f"⚠️  You already guessed {guess}! Try a different number.\n")
                continue  # Don't count duplicate guesses

            # Add this guess to the list of previous guesses
            previous_guesses.append(guess)

            # Step 3: Compare the guess with the secret number
            if guess == secret_number:
                # They got it right!
                guessed = True
                print(f"\n🎉 CORRECT! The number was {secret_number}!")
                print(
                    f"⭐ You got it in {attempts} attempt{'s' if attempts != 1 else ''}!\n")

                # Show performance message based on attempts
                if attempts == 1:
                    print("🤯 Wow! Lucky guess on the first try!")
                elif attempts <= 5:
                    print("🌟 Amazing! You're a great guesser!")
                elif attempts <= 10:
                    print("👍 Good job! You found it!")
                else:
                    print("💪 You got it! Keep practicing to do it faster!")

            elif guess < secret_number:
                # The guess is too low
                print(f"📈 Too low! Try a higher number.")
                print(f"   Attempts so far: {attempts}\n")

            else:
                # The guess is too high
                print(f"📉 Too high! Try a lower number.")
                print(f"   Attempts so far: {attempts}\n")

        except ValueError:
            # This happens if the user enters something that's not a number
            print("❌ Oops! Please enter a valid number (like 50, not 'fifty')\n")
            # Don't count this as an attempt since they didn't enter a valid guess
            continue

    # Step 4: Return the number of attempts
    return attempts


# ===== FUNCTION: PLAY AGAIN? =====

def ask_play_again():
    """
    Asks the user if they want to play again.

    Returns:
    - True if user wants to play again
    - False if they want to quit
    """

    while True:
        # Ask the user
        response = input("\n🎮 Play again? (yes/no): ").lower().strip()

        # Check the response
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("❌ Please enter 'yes' or 'no'")


# ===== FUNCTION: MAIN GAME LOOP =====

def main():
    """
    This is the main function that controls the entire game.
    It lets the user play multiple rounds.
    """

    # Keep track of all games played
    total_games = 0
    total_attempts = 0
    # Start with infinity so any real number is better
    best_game = float('inf')

    # Print header
    print("\n" + "🎮" * 25)
    print("WELCOME TO THE NUMBER GUESSING GAME!")
    print("🎮" * 25)

    # Loop to let user play multiple games
    playing = True
    while playing:

        # Play one game and get the number of attempts
        attempts = play_game()

        # Update statistics
        total_games += 1
        total_attempts += attempts

        # Keep track of best game
        if attempts < best_game:
            best_game = attempts

        # Ask if user wants to play again
        playing = ask_play_again()

    # Game over! Show final statistics
    print("\n" + "=" * 50)
    print("📊 GAME OVER - HERE'S YOUR STATISTICS!")
    print("=" * 50)
    print(f"Total games played: {total_games}")
    print(f"Total guesses made: {total_attempts}")
    print(f"Average guesses per game: {total_attempts / total_games:.1f}")
    print(f"Best game: {best_game} guess{'es' if best_game != 1 else ''}")
    print("=" * 50)
    print("\n🙏 Thanks for playing! Goodbye! 👋\n")


# ===== RUN THE GAME =====
# This only runs if you run THIS file directly
if __name__ == "__main__":
    main()


# ===== HOW THE GAME WORKS STEP-BY-STEP =====
#
# 1. Computer generates a random number (1-100)
#    └─ random.randint(1, 100)
#
# 2. Loop starts (while not guessed:)
#    └─ Keeps asking for guesses until correct
#
# 3. User enters a guess
#    └─ Input is converted from text to number
#
# 4. Computer compares guess to secret number
#    └─ Too low → tell user to go higher
#    └─ Too high → tell user to go lower
#    └─ Correct → congratulate and exit loop!
#
# 5. Repeat until guessed correctly
#
# 6. Ask to play again
#    └─ Yes → Go back to step 1
#    └─ No → Show statistics and quit
#
# ===== KEY PROGRAMMING CONCEPTS =====
#
# random module      → Generates random numbers
# while loop         → Repeats until condition is met
# if/elif/else       → Makes decisions
# try/except         → Handles errors gracefully
# Variables          → Store numbers and text
# Functions          → Organize code into reusable blocks
# Lists              → Keep track of previous guesses
# String methods     → .lower() makes text lowercase
