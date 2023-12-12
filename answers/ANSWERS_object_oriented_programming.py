'''
OBJECT ORIENTED PROGRAMMING PROBLEM ANSWERS
This reviews how to:
- understand conceptually what a class represents
- define a class syntactically
- create instances of classes
- create class attributes, and use them using "self"
- create methods and use methods
'''


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
Would the following be good to define as classes?
- a car                                 - yes
- my favorite word: "platypus"          - no, this would be a string
- how many times I've had a flat tire   - no, this would be an integer
- whether I brought pasta for lunch     - no, this would be a boolean
- a penguin                             - yes
- an exam                               - yes
- my mom's name                         - no, this would be a string
- my parents' wedding date              - no, this would be an instance of a date class, or alternatively a string
- a pet                                 - yes
- a rectangle                           - yes
- a shape                               - yes
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
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def birthday(self) -> None:
        self.age += 1
    def same_name(self, other: 'Person') -> bool:
        return self.name == other.name

rebecca = Person("Rebecca", 80)
rebecca.birthday()
print(rebecca.age) # will print 81
jimmie = Person("Jimmie", 79)
print(rebecca.same_name(jimmie)) # will print false


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
class Shape:
    def __init__(self, num_sides: int, area: float, color: str, side_lengths: [int]):
        self.num_sides = num_sides
        self.area = area
        self.color = color
    def display_info(self) -> str:
        return "This shape has " + self.num_sides + "sides, an area of " + self.area + ", and it's color is " + self.color
    def set_color(self, new_color: str) -> None:
        self.color = new_color
    def same_side_lengths(self, other_side_lengths: [int]) -> bool:
        if len(other_side_lengths) != len(self.side_lengths):
            return False
        for i in range(0, len(self.side_lengths)):
            if (self.side_lengths[i] != other_side_lengths[i]):
                return False
        return True
    def is_same_shape(self, other_shape: 'Shape') -> bool:
        return (self.num_sides == other_shape.num_sides and self.area == other_shape.area
                and self.same_side_lengths(other_shape.side_lengths))
