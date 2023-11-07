# DATA TYPES PROBLEMS

# SECTION 1: DEFINITIONS

# In your own words, what is a number value in Python?
# A number value in Python represents a numerical quantity. 
# Python supports different types of number values, including integers (whole numbers) 
# and floating-point numbers (decimal numbers).


# In your own words, what is a boolean value in Python?
# A boolean value in Python is a data type that can have one of two values: True or False. 


# In your own words, what is a string value in Python?
# A string value in Python is a sequence of characters enclosed within quotes. 
# Strings are used to represent text and are a versatile data type in Python.


# SECTION 2: EXAMPLES

# What are the data types for the following?
# - "hi"             - String
# - 5                - Integer
# - "5"              - String
# - True             - Boolean
# - []               - List
# - ["hi"]           - List
# - ["hi"][0]        - String
# - [5, "hi"]        - List
# - {}               - Dictionary
# - {"hi": "hello"}  - Dictionary
# - {"hi": 5}        - Dictionary

# Give 2 examples of booleans
True
False


# Give 5 examples of numbers
1
42
0
-3
3.14


# Give 5 examples of strings
"Never"
'gonna'
"GIVE"
'u'
"UP <3"


# SECTION 3: NUMBER OPERATIONS

# Do the following described operations on these two numbers:
a = 5
b = 9
# - Check if a is the same as b:                a == b (False)
# - Check if a is greater than b:               a > b (False)
# - Check if a is greater than or equal to b:   a >= b (False)
# - Check if a is less than b:                  a < b (True)
# - Check if a is less than or equal to b:      a <= b (True)
# - Add a and b:                                a + b (14)
# - Subtract a from b:                          b - a (4)
# - Divide b by a:                              b / a (1.8)
# - Multiply a and b together:                  a * b (45)


# Explain the difference between integers and floating-point numbers in Python.
# Integers are whole numbers (e.g., 1, 42), while floating-point numbers (floats) can have decimal points (e.g., 3.14, -0.5)


# Calculate the area of a rectangle with a length of 5.5 units and a width of 3 units
5.5 * 3    # 16.5


# SECTION 4: BOOLEAN OPERATIONS

# - Take the AND of True and True. Also predict the result:   True and True = True
# - Take the AND of True and False. Also predict the result:  True and False = False
# - Take the AND of False and True. Also predict the result:  False and True = False
# - Take the AND of False and False. Also predict the result: False and False = False

# - Take the OR of True and True. Also predict the result:    True or True = True
# - Take the OR of True and False. Also predict the result:   True or False = True
# - Take the OR of False and True. Also predict the result:   False or True = True
# - Take the OR of False and False. Also predict the result:  False or False = False

# - Take the NOT of False. Also predict the result:           not False = True
# - Take the NOT of True. Also predict the result:            not True = False

# What will be the result of this?
not (True and ((True and False) or True))   # False

# Write a function that returns if the given input boolean is TRUE. Don't use an if statement
def is_true(boolean):
  return boolean

# Write a function that returns if the given input boolean is FALSE. Don't use an if statement
def is_false(boolean):
  return not boolean


# SECTION 5: STRINGS

fun_str = "This is a cool funky string!"
# - Use the string substring function to get just "cool" from fun_str:    fun_str[10:14]
# - Use the string length function to get the length of fun_str:          len(fun_str)
# - What is the result of fun_str[5]?                                     'i'
# - Use + to create a new string that is fun_str with ":)" at the end:    fun_str + ":)"
