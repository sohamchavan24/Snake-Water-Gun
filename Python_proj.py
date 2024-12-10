import random
import time

# Display welcome message
print("Welcome to the Snake-Water-Gun Game!")
print("In this game:")
print("Choose 's' for Snake, 'w' for Water, and 'g' for Gun.")
print("Let's see who wins the battle!\n")

# Start the game loop
while True:
    # Get user's choice
    user_choice = input("Enter your choice (s/w/g): ").lower()
    while user_choice not in ['s', 'w', 'g']:
        print("Invalid choice! Please choose 's' for Snake, 'w' for Water, or 'g' for Gun.")
        user_choice = input("Enter your choice (s/w/g): ").lower()

    # Get computer's choice
    options = ['s', 'w', 'g']
    computer_choice = random.choice(options)

    # Display choices
    choices_map = {'s': 'Snake🐍', 'w': 'Water💧', 'g': 'Gun🔫'}
    print(f"\nYou chose {choices_map[user_choice]}!")
    time.sleep(1)
    print(f"The computer chose {choices_map[computer_choice]}!\n")
    time.sleep(1)

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 's' and computer_choice == 'w') or (user_choice == 'w' and computer_choice == 'g') or (user_choice == 'g' and computer_choice == 's'):
        print("You win! 🎉")
    else:
        print("Computer wins! 💻")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thank you for playing Snake-Water-Gun! Goodbye! 👋")
        break
