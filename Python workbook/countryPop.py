countryPop = {"Japan":"127000000", "Germany":"81000000", "Iran":"77000000",
              "UK":"64000000", "Canada":"33000000", "Australia":"23000000", "USA":"317000000",
              "Bulgaria":"7000000", "Sweden":"10000000"}

print("Welcome! Let's calculate the combined population of two countries.\n")
print("Available countries:")
for country in countryPop:
    print("-", country)
    
# Get first country
first_country = input("\nPlease enter the name of the **first** country: ")
while first_country not in countryPop:
    print("That country is not in the list. Please try again.")
    first_country = input("Enter a valid country name: ")
    
# Get second country
second_country = input("Please enter the name of the **second** country: ")
while second_country not in countryPop:
    print("That country is not in the list. Please try again.")
    second_country = input("Enter a valid country name: ")
    
# Add populations
population1 = int(countryPop[first_country])
population2 = int(countryPop[second_country])
total_population = population1 + population2

#Display result
print(f"\nThe combined population of {first_country} and {second_country} is {total_population:,} people.")
