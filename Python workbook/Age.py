# Import the 'date'class from the 'datetime' module to 
from datetime import date

# Prompt the user to enter their birthdate
print("Enter your birthdate:")

# Get the birth year from the user and covert it to an integer
year = int(input("Enter your birth year (e.g.,2000): "))

# Get the birth month from the user and convert it to an integer
month = int(input("Enter your birth month (1-12): "))

# Get the birth day from the user and convert it to an integer
day = int(input("Enter your birth day (1-31): "))

# Create a date object for the user's birthdate
birthdate = date(year, month, day)

# Get today's current date
today = date.today()

# Calculate the number of the days the user has lived by subtracting birthdate from today's date
days_lived = (today - birthdate).days

# Display the result
print("You have lived for", days_lived, "days.")