# Step 3: Add 4 new numbers and update the file
with open("numbers.txt", "r") as file:
    numbers = [float(line.strip()) for line in file]
    
for i in range(4):
    num = float(input(f"Enter ne number {i + 1}: "))
    numbers.append(num)
    
# Write updated list back to the file
with open("numbers.txt", "w") as file:
    for number in numbers:
        file.write(f"{number} \n")
        
print("Updated list written to file.")

