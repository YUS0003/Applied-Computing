# Ask the user how many people the money should be shared with and convert the input to an integer
shares = int(input("How many people do you want to share the money with? "))

# Divide 1000 by the number of people to calculate the amount each person gets
money = 1000/shares

# Print the calculated amount of money per person
print(money)
