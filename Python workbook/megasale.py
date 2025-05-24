# Ask the user to enter the amount of money the customer spent and convert it to a float
amount = float(input("Enter the amount spent by the customer: "))

# If the amount is greter than $20, the customer gets a $3 voucher
if amount > 20:
    print("Give $3 voucher")
    
# If the amount is not over $20 but is greater than $10, the customer gets a $1 voucher    
elif amount > 10:
    print("Give $1 voucher")
    
# If the amount is $10 or less, the cutomer does not get a voucher
else:
    print("No voucher")