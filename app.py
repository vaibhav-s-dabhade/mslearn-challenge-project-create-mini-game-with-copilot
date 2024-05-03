#  Specification
# As we learned in the introduction to this challenge, the winner of the game is determined by three simple rules:

# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
# What you should consider in the game interactions
# Let's add some more excitement to this challenge and make the game multiplayer, where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console (Terminal).

# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

#Write the code as per above specification and steps provided

# Step 1: Define the game rules
# Define the rules of the game in a dictionary where the key is the element and the value is a list of elements that the key can beat.

# Step 2: Define the game interactions
# Create a function that will handle the game interactions. The function should:
# Print the game rules.
# Ask the player to choose an element.
# Randomly choose an element for the computer.
# Determine the winner based on the game rules.
# Display the result of the round.
# Ask the player if they want to play again.
# Keep track of the player's score.
# Step 3: Implement the game logic
# Implement the game logic based on the defined rules and interactions.

# Step 4: Run the game
# Run the game and test the player's interactions.
import random

def game():
    # Define the game rules
    rules = {
        'rock': ['scissors'],
        'scissors': ['paper'],
        'paper': ['rock']
    }

    # Initialize the player's score
    player_score = 0

    # Game interactions
    while True:
        print("Welcome to Rock, Paper, Scissors!")
        print("Game rules:")
        print("Rock beats scissors.")
        print("Scissors beats paper.")
        print("Paper beats rock.")
        print("Enter 'quit' to exit the game.")

        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice == 'quit':
            break

        if player_choice not in rules:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(list(rules.keys()))

        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif computer_choice in rules[player_choice]:
            print("You win!")
            player_score += 1
        else:
            print("You lose!")

        print(f"Your score: {player_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != 'yes':
            break

    print("Thanks for playing!")

game()





