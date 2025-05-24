# Step 2: Read the file and display each person's data
with open("people.txt", "r") as file:
    for line in file:
        name, height, weight = line.strip().split(",")
        print(f"Name: {name}, Height: {height}, Weight: {weight}")
        