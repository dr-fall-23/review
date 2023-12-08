'''
OBJECT ORIENTED PROGRAMMING PROBLEMS
This reviews how to:
- understand conceptually what a class represents
- define a class syntactically
- create instances of classes
- create class attributes, and use them using "self"
- create methods and use methods
'''

# INTRO:
# Here's an example of a class:
class Square:
    def __init__(self, color: str, side_length: int):
        self.color = color
        self.side_length = side_length
    def increase_size_by(self, increase):
        self.side_length += increase
    def is_color(self, other_color: str) -> bool:
        return self.color == other_color
    def same_square(self, other: 'Square') -> bool:
        return self.is_color(other.color) and self.side_length == other.side_length
# This class represents a square shape that has a side length and color.
# The side length can increase, the color can be compared to another color, and the square can be compared to anther square
# (Note: we need to use single quotes around 'Square' in the input types for same_square because of a funky thing in Python
#  called forward references. Don't worry too much about that for now)

# We use classes to represent abstract real world ideas: things like a Student, a Square, a Car, etc.
# Like strings, booleans, integers, etc, objects are a type of data, but they're much more complex.

# Here's an example of creating an "instance" of the class Square. We also call this "instantiating"
my_square = Square("red", 40)
# We can create as many instances as we want!
my_green_square = Square("green", 40)
smol_square = Square("red", 2)


# Here is an example of a car class
class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year =  year
    def __repr__(self):
        return str(self.year) + " " + self.make + " " + self.model
    def honk(self):
        print("BEEEEEP!")

# What are all of the attributes in this class
#? make, model and year
# What are all of the methods
#? init, repr, and honk

'''
Problem 1.
Would the following be good to define as objects?
- a car                                 -
- my favorite word: "platypus"          -
- how many times I've had a flat tire   -
- whether I brought pasta for lunch     -
- a penguin                             -
- an exam                               -
- my mom's name                         -
- my parents' wedding date              -
- a pet                                 -
- a rectangle                           -
- a shape                               -
'''


'''
Problem 2:
Create a class called Person with attributes name and age.
Include a method called birthday that increments the age of the person by 1.
Instantiate ("create an instance of") an object of the class, set its initial values, and then call the birthday method.
Create another method "same_name" that takes in a Person (use 'Person' as the type not just Person) and returns whether
they have the same name as this person.
Create another instance of a Person, and then check if they have the same name using the first person's "same_name" method.
'''



'''
Problem 3:
Create a class named Shape with the following attributes: num_sides, area, and color.
Create a method called "display_info" that prints out the information about the shape.
Create another method "set_color" that takes in a string representing a color and sets the shape's color to
this new string.
Create another method "is_same_shape" that takes in another Shape (use type 'Shape' not just Shape) and returns
if they have the same num_sides and area (shape color doesn't matter here for equality).

Now, add another attribute "side_lengths" to the a Shape (hint: add to __init__), which will be a list of integers
representing the lengths of each of its sides.
Now create a "same_side_lengths" method that takes in another list of integers representing side lengths.
Now use "same_side_lengths" in the "is_same_shape" method.
'''
