# Step 2: Read numbers from file, calculate total and average
with open("numbers.txt", "r") as file:
    numbers = [float(line.strip()) for line in file]

print("Numbers read from file:", numbers)

total = sum(numbers)
average = total / len(numbers)

print(f"Total: {total}")
print(f"Average: {average}")

# Sort the numbers
numbers.sort()
print("Sorted numbers (ascending):", numbers)


               