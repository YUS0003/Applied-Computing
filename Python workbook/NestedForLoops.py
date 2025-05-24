# Times tables from 1 to 12 using nested loops
for i in range(1, 13): # Outer loop for the base number (1 to 12)
    print(f"{i} Times Table:")
    for j in range(1, 13): # Inner loop for the multiplier (1 to 12)
        print(f"{i} * {j} = {i * j}")
    print() # Print a blank line after each table
    