# VARIABLES PROBLEMS

# In the following line of code, what happens?
# print(x)
# The program throws an error if you run this, because x isn't defined. The program has no idea what x is
# This is an example of assigning a value, the number 4, to a variable to named x
x = 4
# The = operator means "assignment". Previously, x in our code had no meaning, but now x is 4
# If we call the following line, the program prints 4
print(x)
# This is called "using a variable" or "referencing a variable"
# If we call the following line, the program prints 6, because behind the scenes it's doing 4 + 2
print(x + 2)

# There's a lot of different language used to describe this concept, so here are some synonyms for "assign":
# - "assign ___ to x"
# - "set x to ___"
# - "initialize x as ___"
# - "give x a value of ___"
# - "store ___ inside x"
# - "define x as ___"

# SECTION 1: VARIABLE BASICS

# Define a variable named my_name and assign it to a string representing your full name (first and last name)
my_name = "Rebecca Swernofsky"


# Print your full name by referencing your new my_name variable
print(my_name)


# Print the substring of just your last name by referencing my_name
print(my_name.substring(7))


# Now store your last name substring in a new variable called last_name
last_name = my_name.substring(7)


# Print the substring of just your last name WITHOUT referencing my_name
print("Rebecca Swernofsky".substring(7))


# SECTION 2: UPDATING VARIABLES

y = 1      # here we define y as 1
print(y)   # we print y and we get 1
y = 2      # here we REDEFINE y as 2
print(y)   # here we get 2, because y is now 2
# We can redefine variables as many times as we want! You hold the power mwahahaha
y = y + 1  # y on the right side of the = has a value of 2, but after this line, y will be redefined with a new value
# We can use the same variable when redefining it!

# Set a variable my_favorite_num to your favorite number
my_favorite_num = 27


# Oh my! Somehow we got sucked forward in time several years, and now your favorite number is something different.
# Redefine my_favorite_num to be another number
my_favorite_num = 3


# Now it's the next day, and your favorite number is 5 more than it was yesterday. You can't remember what
# number it was yesterday though, so instead you decide to use my_favorite_num to define the new value of my_favorite_num.
# Redefine my_favorite_num to be 5 more than my_favorite_num's current value
my_favorite_num = my_favorite_num + 5


# SECTION 3: NAMING CONVENTIONS

# When naming variables in python, it's standard practice to use CAPS LOCK for variables that will never change:
CIRCLE_PIXEL_RADIUS = 50
# When naming other variables, we use lower case and "snake case" (multiple words are separated using underscores):
item_count = 4
current_name = "Joseph"
is_player_alive = True
# We also try to have our variable names be descriptive. Something like length_in_feet is better than x


# Create a CONSTANT variable representing the number of wheels on a typical car
AVERAGE_WHEELS = 4


# Create a variable that will change often, representing the age of your youngest sibling
youngest_sibling_age = 14
