# FUNCTION INPUT/OUTPUT PROBLEMS

# This is an example of a function
# In words, it takes in an input string, and if the string is "hello", the function returns "yayy"
# Otherwise, the function returns "awww :("
def func(input: str) -> str:
  if (str == "hello"):
    return "yayy"
  else:
    return "awww :("

# Functions don't strictly NEED input and output types to be specified, but it's considered "good practice" to
# The following will work the same and are both valid:
def add_nums(a: int, b: int) -> int:
  return a + b

def add_nums2(a, b):
  return a + b

# Based on this code snippet, describe in words that this function takes in, and what it outputs
def household_size(date: str, address: str) -> int:
  ...
# inputs: a date as a string and an address as a string. the output is an integer (the size)

#? Describe the difference between func_a and func_b
def func_a(input: str) -> str:
  return input

def func_b(input: str) -> None:
  print(input)

# func_a returns the input and func_b prints the input to the console

# Write a function that takes in a string and returns that given string
def parrot(x):
  return x


# Write a function that takes in a number, but always returns the string "nice!"
def nice(num):
  return "nice!"


# Write a function that takes in a number, prints the given number, and then returns the string "nice!"
def print_and_nice(num):
  print(num)
  return "nice!"


# Write a function that takes in a number, prints the given number, and then returns nothing
def print_num(num):
  print(num)


# What will the output of this code snippet be?
def outer_fun(a, b):
  def inner_fun(c, d):
    return c + d
  return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)
# 15. outer_fun will call inner_fun with c = 5 and d = 10. inner_fun(5, 10) is 15, so
# return inner_fun(a, b) will mean outer_fun returns 15


# Describe what this function is doing:
def my_func(a: int, b: [str]) -> bool:
  counter = 0
  for x in b:
    if 'c' in x:
      counter += 1
  return counter == a

# a good way to understand what this does is to test it!
print(my_func(2, ['c', 'c'])) # true
print(my_func(2, ['c', 'cc'])) # true
print(my_func(2, ['cc', 'a'])) # false
print(my_func(2, ['c', 'a'])) # false
print(my_func(2, ['c', 'a', 'b'])) # false
# my_func checks if there are *a* number of elements in *b* list that contain a 'c'
# it does this by counting the number of elements in *b* that contain 'c', and then compares the counter to *a*


# Fill in the types for this functions inputs and outputs
def mystery_function(a: int, b: bool, c: str) -> str:
  if a > 14 and not b:
    return c.substring(1)
  else:
    return "oof"
# modify the def mystery_function(...) line to look like:
# def mystery_function(a: __, b: __, c: __) -> __:
# fill in the blanks