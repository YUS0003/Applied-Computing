# Define the correct password that will be used for comparison
secret_password = "pocketrocket96"

# Prompt the user to enter a password and store their input
entered_password = input("Enter the secret password: ")

# Check if the entered password matches the secret password
if entered_password == secret_password:
    # If the passwords match, grant access
    print("Access granted! Welcome to the program.")
    
else:
    # If the passwords do not match, deny access
    print("Access denied! Wrong password.")