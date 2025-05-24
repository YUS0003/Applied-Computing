# Print a message to introduce the purpose of the program
print("Dinner and taxi ride calculation.")

# Ask the user how many people are sharing the cost and convert the input to an integer
people = int(input("How many people? "))

# Ask for the total dinnner bill and convert it to a float (for decimal values)
bill = float(input("How much is the bill? $"))

# Ask the user for the tip percentage and convert it to a float
tip = float(input("What tip percentage? "))

# Ask how many miles were traveled in the taxi and convert it to a float
miles = float(input("How many miles in the taxi? "))

# Calculate the total bill including the tip
total_bill = bill * (1 + tip / 100)

# Calculate the cost of the taxi ride at $0.45 per mile
taxi_cost = miles * 0.45

# Calculate the total cost for the evening (dinner + taxi)
total_evening = total_bill + taxi_cost

# Divide the total cost evenly among the people
each_person_pays = total_evening / people

# Print the total cost of the evening, rounded to 2 decimal places
print(f"\nTotal evening cost: ${round(total_evening, 2)}")

# Print how much each person should pay, rounded to 2 decimal places
print(f"Each person pays: ${round(each_person_pays, 2)}")









