# Display the title of the program
print("YOUR NAME'S calories counter")

# Prompt the user to input the number of calories they've eaten today, and convert the input to an integer
calories = int(input("How many calories have you eaten today? "))

# Calculate how many calories the user can still eat today, assuming a 2000 calorie daily limit
s = 2000-calories

# Display the remaining calories the user can consume
print("You can eat",s, "more calories today")