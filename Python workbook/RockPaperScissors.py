import random

# Ask the player for their name
player_name = input("Enter your name: ")

# Ask how many rounds to play (between 3 and 10)
while True:
    try:
        total_rounds = int(input("How many rounds would you like to play (3-10)? "))
        if 3 <= total_rounds <= 10:
            break # valid input
        else:
            print("Please enter a number between 3 and 10.")
    except ValueError:
        print("That's not a valid number. Please enter a number between 3 and 10.")
# Initialise scores
player_score = 0
computer_score = 0

# List of valid moves
moves = ["rock", "paper", "scissors"]

# Game loop
for round_num in range(1, total_rounds + 1):
    print(f"\n--- Rounds {round_num} ---")
    
    # Get's player's move
    player_move = input("Choose rock, paper, or scissors: ").lower()
    while player_move not in moves:
        player_move = input("Invalid input. Please choose rock, paper, or scissors: ").lower()
        
    # Get computer's move
    computer_move = random.choice(moves)
    print(f"{player_name} chose {player_move}")
    print(f"Computer chose {computer_move}")
    
    # Determine winner
    if player_move == computer_move:
        print("It's a draw!")
    elif(player_move == "rock" and computer_move == "scissors") or \
        (player_move == "paper" and computer_move == "rock") or \
        (player_move == "scissors" and computer_move == "paper"):
        print(f"{player_name} wins this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
        
    # Display current score
    print(f"Score => {player_name}: {player_score}, Computer: {computer_score}")
    
    # Final results
    print("\n--- Game Over ---")
    print(f"Final Score => {player_name}: {player_score}, Computer: {computer_score}")
    
    if player_score > computer_score:
        print(f"Congratulations {player_name}, you won this game!")
    elif player_score < computer_score:
        print("Computer wins the game! Better luck next time.")
    else:
        print("It's a tie!")
        