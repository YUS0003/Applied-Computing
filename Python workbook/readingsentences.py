# Ask the user to enter a sentence
sentence = input("Type a sentence: ")

# Initialise the counter
numberE = 0

# Loop through each character in the sentence
for letter in sentence:
    if letter == "e":
        numberE += 1

# Display the result
print("The number of 'e's in the sentence is: ", numberE)