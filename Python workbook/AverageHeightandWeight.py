# Calculate average height and weight (overall and by gender)

male_names = ["James", "Peter", "Jay"]
female_names = ["Beth", "Mags", "Joy"]

total_height = 0
total_weight = 0
count = 0

male_height = 0
male_weight = 0
male_count = 0

female_height = 0
female_weight = 0
female_count = 0

with open("people.txt", "r") as file:
    for line in file:
        name, height, weight = line.strip().split(",")
        height = int(height)
        weight = float(weight)
        
        # Add to overall totals
        total_height += height
        total_weight += weight
        count += 1
        
        # Gender-based logic
        if name in male_names:
            male_height += height
            male_weight += weight
            male_count += 1
        elif name in female_names:
            female_height += height
            female_weight += weight
            female_count += 1
            
# Display averages
print(f"\nAverage height (all): {total_height / count: 2f}")
print(f"Average weight (all): {total_weight / count:.2f}")

if male_count > 0:
    print(f"\nAverage height (men): {male_height / male_count: 2f}")
    print(f"Average weight (men): {male_weight / male_count:.2f}")
    
if female_count > 0:
    print(f"\nAverage height (women): {female_height / female_count: 2f}")
    print(f"Average weight (women): {female_weight / female_count:.2f}")
    

    