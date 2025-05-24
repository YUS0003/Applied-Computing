# Step 1: Enter the list and store it in a file

# Raw data list
heightandweight = [
    "James", 73, 1.82,
    "Peter", 78, 1.80,
    "Jay", 70, 1.75,
    "Beth", 65, 1.53,
    "Mags", 66, 1.50,
    "Joy", 62, 1.34
]

# Write to file: name, height, weight format
with open("people.txt", "w") as file:
    for i in range(0, len(heightandweight), 3):
        name = heightandweight[i]
        height = heightandweight[i + 1]
        weight = heightandweight[i + 2]
        file.write(f"{name},{height},{weight}\n")
        
print("Data written to file.")
































