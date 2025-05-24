# Set your own first name
my_name = "Aden"

# Loop until the correct name is entered
while True:
    # Ask the user for their first name
    user_name = input("Please enter your first name: ")
    
    # check if it matches your name
    if user_name == my_name:
        print("Welcome,", my_name + "! You guessed correctly.")
        break # Exit the loop
    
    else:
        print("Sorry, that's not the name I'm looking for. Please try again.")