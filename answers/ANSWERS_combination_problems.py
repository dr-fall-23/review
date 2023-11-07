# COMBINATION PROBLEMS
# These problems will be a mix of many concepts you've learned so far, all mixed together
# For each exercise, unless explicitly asked, don't reuse the functions written for previous questions to answer
# other questions

# SECTION 1

# Write a function that takes in a list of numbers and returns that list
def return_list(lst):
  return lst


# Write a function that takes in a list of numbers and prints every element in that list
# Don't return anything
def print_elements(lst):
  for num in lst:
    print(num)


# Write a function that takes in a list of numbers and returns the length of the list
def list_len(lst):
  return len(lst)


# Write a function that takes in a list of numbers and prints every element in that list
# Return the total number of elements in the list (the length)
def print_elements(lst):
  for num in lst:
    print(num)
  return len(lst)


# Write a function that returns the sum of all numbers in a given list of numbers
def sum_list(lst):
  result = 0
  for num in lst:
    result += num
  return result


# Write a function that returns the sum of all EVEN numbers in a given list of numbers
# Do not use a helper function to check even-ness
def sum_list(lst):
  result = 0
  for num in lst:
    if (num % 2 == 0):
      result += num
  return result


# Write a function that returns the sum of all EVEN numbers in a given list of numbers
# DO use a helper function to check even-ness
def is_even(num):
  return num % 2 == 0

def sum_list(lst):
  result = 0
  for num in lst:
    if is_even(num):
      result += num
  return result


# SECTION 2

# Write a function that returns the number of strings in a given list of strings that contain the word "grey"
# Use a helper function
# Use the following steps:
# - determine what the input and output of the function should be
# - create a variable that stores the current count of satisfactory strings (strings that contain the word "grey")
# - loop through the list
# - create a helper function that tests if a string contains the word "grey"
# - inside the loop, use an in if statement to check if each string element of the list is "satisfactory".
#   if it is, add 1 to the counter
# - outside the loop (after the loop), return the answer (stored in the counter)
def contains_grey(string):
  return "grey" in string

def count_grey_strings(lst):
  counter = 0
  for string in lst:
    if contains_grey(string):
      result += 1
  return counter


# SECTION 3

# Write a function that takes in a string that is either "red", "yellow", or "green", and returns true if a car may
# proceed through the intersection
def can_go(color: str) -> bool:
  return (color == "red") or (color == "yellow")


# Write a function that takes a sentence as input and counts the number of vowels (a, e, i, o, u) in the sentence
def count_vowels(sentence):
  vowels = "aeiou"
  count = 0
  for char in sentence:
    if char.lower() in vowels:
      count += 1
  return count


# Write a function that returns the average of all numbers in a list
def calculate_average(numbers):
  num_elements = len(numbers)
  if num_elements == 0:
    return 0  # Handle the case when the input list is empty to avoid division by zero
  total = sum(numbers)
  average = total / num_elements
  return average


# Write a function that checks if at least half of the number of elements in a given list are even
def is_half_elements_even(input_list):
  total_elements = len(input_list)
  
  even_count = 0
  for num in input_list:
    if num % 2 == 0:
      even_count += 1
  
  if even_count >= total_elements / 2:
    return True
  else:
    return False