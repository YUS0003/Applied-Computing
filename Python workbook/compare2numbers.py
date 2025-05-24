# Prompt the user to enter the first number and convert it to a float
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number and convert it to a float
num2 = float(input("Enter the second number: "))

# Check if the first number is greater than the second number
if num1 > num2:
    print(num1, "is greater than", num2)
    
# Check if the first number is less than the second number  
if num1 < num2:
    print(num2, "is greater than", num1)
    
# Check if both numbers are equal    
if num1 == num2:
    print(num1, "is equal to", num2)