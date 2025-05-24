# Ask the user to enter a sentence
sentence = input("Type a sentence: ")

# Initialise the counter
vowel_count = 0

# Define the set of vowels
vowels = "aeiou"

# Loop through each character in the sentence
for letter in sentence.lower(): # Convert to lowercase for case-sensitive comparison
    if letter in vowels:
        vowel_count += 1
        
# Display the result
print("The number of vowels in the sentence is: ", vowel_count)
