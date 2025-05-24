# Ask the user for the number
number = int(input("Enter the number for your times table (e.g., 1345): "))

# Loop through 1 to 12 and print the times table
print(f"\n{number} Times Table:")
for i in range(1, 13):
    print(f"{number} * {i} = {number * i}")
    