# Enter a number between 1 and 10
number = 40

while number not in range (1,11):
    try:
        number = int(input("Please enter a number between 1 and 10"))
        
    except:
        print("ERROR invalid input. Out of range or wrong type of data.")
        
print("Thank you I have recorded your entry as:", number)
