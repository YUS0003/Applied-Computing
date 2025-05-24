# function to calculate area
def area(length, width):
    shapeArea = length * width
    print("Area = ", shapeArea)
    
def perimeter():
    shapePerimeter = length * 2 + width * 2 
    print("Perimeter = ", shapePerimeter)
    
response = None
while response not in ("a","p"):
    response = input("Do you want to calculate area or perimeter? Enter a or p")
    response = response.lower()
    
if response == "a":
    length = int(input("Enter the length of the rectangle"))
    width = int(input("Enter the width of the rectangle"))
    area(length, width)
    
elif response == "p":
    perimeter()
    
    
    
    