# Step 1: Get 6 numbers and write to a file
numbers = []

for i in range(6):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)
    
# Write numbers to a file
with open("numbers.txt", "w") as file:
    for number in numbers:
        file.write(f"{number}\n")
        
print("Numbers written to a file.")
