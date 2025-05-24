import turtle

wn = turtle.Screen()
tom = turtle.Turtle()

def square(length):
    for a in range (4):
        tom.forward(length)
        tom.right(90)
    wn.exitconclick()
    
size = int(input("Enter the length of the square"))
square(size)
    
        

        