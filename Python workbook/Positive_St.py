# Import the 'random' module which provides functions to generate random numbers and choices
import random

# Create a list named 'student_names' containing ten student names
student_names = ['Andrew', 'Bobby', 'Renato', 'Tracey', 'Adam', 'Michael', 'Nicci', 'Mary', 'Lance', 'Soula']

# Import the 'choice' function specifically from the 'random' module
from random import choice

# Use the 'choice' function to selet and print a random element from the 'letter' list
print(choice(student_names))

