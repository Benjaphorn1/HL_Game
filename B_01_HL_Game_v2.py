import math
import random

# Check that users have entered a valid option based on a list
def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:
        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # Check if the user response is a word in the list
            if item == user_response:
                return item

            # Check if the user response is the same as the first letter of an item in a list
            elif user_response == item[0]:
                return item

        # Print error message if something isn't valid
        print(error)
        print()

# Checks for an integer more than 0 (allows <enter>)
def int_checker(question, low=None, high=None, exit_code=None, default_low=None, default_high=None):
    """Checks user enters an integer within a specified range or uses default values."""

    # Define error message based on the parameters
    if low is None and high is None:
        error = "Please enter an integer."
    elif low is not None and high is None:
        error = f"Please enter an integer that is more than or equal to {low}."
    else:
        error = f"Please enter an integer between {low} and {high} (inclusive)."

    while True:
        response = input(question).lower()

        # Check for exit code
        if response == exit_code:
            return exit_code

        # Handle empty input for default values
        if response == "":
            if default_low is not None:
                return default_low
            elif default_high is not None:
                return default_high
            else:
                print(error)
                continue

        try:
            response = int(response)

            # Check if the integer is within the specified range
            if low is not None and response < low:
                print(error)
            elif high is not None and response > high:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

def instructions():
    """Prints instructions for the game."""
    print("""
 *** Instructions ***

 To begin, choose the number of rounds and either customise
 the game parameters or go with the default game (where the
 secret number will be between 1 and 100).
 
 Then choose the number of rounds you'd like to play or 
 <enter> for infinite mode.
 
 Your goal is to try guess the secret number without 
 running out of guesses.
 
 Good luck!
    """)

# Calculate number of guesses allowed
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses

# Main routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
rounds_won = 0
rounds_lost = 0
game_history = []

print()
print("-Welcome to the Higher Lower Game-")

# Ask user if they want instructions
want_instructions = string_checker("Do you want to see instructions? ")

# If user says yes, display instructions
if want_instructions == "yes":
    instructions()

# Main game loop
while True:
    # Ask user for number of rounds / infinite mode
    num_rounds = int_checker("How many rounds would you like? Push enter for infinite mode: ",
                             low=1, exit_code="")

    if num_rounds == "":
        mode = "infinite"
        num_rounds = 5

    # Get game parameters with default values
    low_num = int_checker("Low Number? (Press <Enter> for default 0): ", default_low=0)
    high_num = int_checker("High number? (Press <Enter> for default 10): ", low=low_num + 1, default_high=10)

    # Game loop starts here
    while rounds_played < num_rounds:

        # Rounds heading
        if mode == "infinite":
            rounds_heading = f"\n Round {rounds_played + 1} (Infinite mode)"
        else:
            rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds}"

        print(rounds_heading)
        print()

        rounds_played += 1

        # If users are in infinite mode, increase number of rounds
        if mode == "infinite":
            num_rounds += 1

        # Reset guesses and secret number for each round
        guess_allowed = calc_guesses(low_num, high_num)  # Recalculate guesses for each round
        secret = random.randint(low_num, high_num)  # New secret number for each round
        guesses_used = 0  # Reset guesses used
        already_guessed = []  # Reset already guessed numbers

        guess = ""
        while guess != secret and guesses_used < guess_allowed:

            # Ask user to guess the number
            guess = int_checker("Guess: ", low_num, high_num, "xxx")

            # Check that they don't want to quit
            if guess == "xxx":
                end_game = "yes"
                break

            # Check that guess has not been guessed yet
            if guess in already_guessed:
                print(f" You've already guessed {guess}. You've still used "
                      f"{guesses_used} / {guess_allowed} guesses")
                continue

            # If guess is not a duplicate, add it to the list
            else:
                already_guessed.append(guess)

            # Add one to the number of guesses used
            guesses_used += 1

            # Compare user's guess with the secret number and set up feedback statement
            if guess < secret and guesses_used < guess_allowed:
                feedback = (f"Too low! Please try a higher number! "
                            f"You've used {guesses_used} / {guess_allowed} guesses")
            elif guess > secret and guesses_used < guess_allowed:
                feedback = (f"Too high! Please try a lower number! "
                            f"You've used {guesses_used} / {guess_allowed} guesses")
            elif guess == secret:
                if guesses_used == 1:
                    feedback = "Lucky! You got it on the first try!"
                    rounds_won += 1
                    result = "Won"
                elif guesses_used == guess_allowed:
                    feedback = f"Phew! You got it in {guesses_used} guesses"
                    rounds_won += 1
                    result = "Won"
                else:
                    feedback = f"Well done! You guessed the secret number in {guesses_used} guesses"
                    rounds_won += 1
                    result = "Won"
            else:
                feedback = "Sorry, you have no guesses left. You lost!"
                rounds_lost += 1
                result = "Lost"

            # Print feedback to user
            print(feedback)

            # Additional feedback
            if guesses_used == guess_allowed - 1:
                print("\n Careful, you have one guess left\n")

        # Add round result to game history
        game_history.append(f"Round {rounds_played}: {result}")

        print()
        print("End of round")

        # Check if the user wants to exit the game
        if guess == "xxx":
            break

    # Game loop ends here

    # Game history / Statistics area
    if rounds_played > 0:
        # Calculate statistics
        percent_won = rounds_won / rounds_played * 100
        percent_lost = rounds_lost / rounds_played * 100

        # Output game statistics
        print("📊📊📊 Game Statistics 📊📊📊")
        print(f"👍 Won: {percent_won:.2f}% \t "
              f"😢 Lost: {percent_lost:.2f}%")

        # Ask user if they want to see game history
        want_history = string_checker("Do you want to see game history? ")

        # Output history if user says yes
        if want_history == "yes":
            print("\n---Game History---")
            for item in game_history:
                print(item)

        print()
        print("Thanks for playing!")
    else:
        print("🐔🐔🐔 Oops! - You chickened out! 🐔🐔🐔")

    # Ask user if they want to play again
    play_again = string_checker("Do you want to play again? (yes/no): ")
    if play_again == "no":
        print("Thanks for playing!")
        break
    else:
        # Reset game variables for a new game
        mode = "regular"
        rounds_played = 0
        rounds_won = 0
        rounds_lost = 0
        game_history = []
        print("Let's play again!")