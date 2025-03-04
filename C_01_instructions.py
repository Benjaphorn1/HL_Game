# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same
            # as the first letter of an item in a list
            elif user_response == item[0]:
                return item

        # print error message if something isn't valid
        print(error)
        print()


def instructions():
    """prints instructions"""

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


# main routine starts here
print()
print("🔺🔺🔺Welcome to the higher lower game!⬇️⬇️⬇️")
print()

# ask user if they want instructions
want_instructions = string_checker("Do you want to see instructions? ")

# if user says yes display instructions
if want_instructions == "yes":
    instructions()

print("Program continues")
