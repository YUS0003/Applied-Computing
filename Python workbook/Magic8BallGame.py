import random # Importing the random module to generate random numbers

# Predifined responses from the Magic 8 Ball
answer1 = ("Absolutely!")
answer2 = ("No way Pedro!")
answer3 = ("Go for it tiger.")
answer4 = ("You really think i'm going to help you out.")
answer5 = ("I don't care, watch this Magic 8 Ball shake!")

# Print a welcome message for the user
print("Welcome to the Magic 8 Ball game - use it to answer your questions...")

# Prompt the user to ask a question
question = input("Ask me for any advice and i'll help you out. Type in your question and then press Enter for an answer.")

# Simulate the "shaking" of the Magic 8 Ball
print("shaking....\n" * 4)

# Generate a random number between 1 and 3 (inclusive)
choice = random.randint(1,3)

# Determine which answer to display based on the random number
if choice == 1:
    answer = answer1
    
elif choice == 2:
    answer = answer2
    
elif choice == 3:
    answer = answer3
    
elif choice == 4:
    answer = answer4
    
else:
    answer = answer5
    
# Display the chosen answer to the user
print(answer)