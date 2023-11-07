# Function Input/Output Extra Practice

# This is an example of a function
# In words, it takes in an input string, and if the string is "hello", the function returns "yayy"
# Otherwise, the function returns "awww :("
def func(input: str) -> str:
  if (str == "hello"):
    return "yayy"
  else:
    return "awww :("


# Based on this code snippet, describe in words that this function takes in, and what it outputs
def household_size(date: str, address: str) -> int:
  ...


# Write a function that takes in a string and returns that given string


# Write a function that takes in a number, but always returns the string "nice!"


# Write a function that takes in a number, prints the given number, and then returns the string "nice!"


# Write a function that takes in a number, prints the given number, and then returns nothing


# What will the output of this code snippet be?
def outer_fun(a, b):
  def inner_fun(c, d):
    return c + d
  return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)


# Describe what this function is doing:
def my_func(a: int, b: [str]) -> bool:
  counter = 0
  for x in b:
    if 'c' in x:
      counter += 1
  return counter == a

  
