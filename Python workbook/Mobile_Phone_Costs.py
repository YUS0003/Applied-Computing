# Ask the user how many pictures they send per month and convert the input to an integer 
pictures = int(input("How many pictures do you send per month? "))

# Ask the user how many text messages they send per month and convert the input to an integer
texts = int(input("How many text messages do you send per month? "))

# Ask the user how much data (in MB) they use per month and convert the input to a float
data = float(input("How many data (in MB) do you use per month? "))

# Calculate the total cost of sending pictures at $0.35 each
picture_cost = pictures * 0.35

# Calculate the total cost of sending text messages at $0.10 each
text_cost = texts * 0.10

# Calculate the total cost of using  data at $0.05
data_cost = data *0.05

# Add up the individual cots to get the total monthly cost
total_cost = picture_cost + text_cost + data_cost

# Print the total monthly bill, formatted to two decimal places
print(f"\nYour total monthly bill would be: ${total_cost:.2f}")

# Suggest a contract plan if the total monthly cost is more than $10
if total_cost > 10:
    print("You would be better off on a contract plan.")
    
# Suggest staying on pay-as-you-go if the cost is $10 or less   
else:
    print("Pay-as-you-go seems fine for now.")