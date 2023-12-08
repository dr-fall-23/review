# LOOPS PROBLEMS

# SECTION 1:

# Explain the purpose of a for loop in Python, and how it works
# A for loop in Python is used for iterating over a sequence (such as a list, tuple, string, or range)
# or other iterable objects. It allows you to execute a block of code repeatedly for each item in the sequence.
# The loop iterates through each element in the sequence and executes the specified block of code
# until the sequence is exhausted.


# Explain the purpose of a while loop in Python, and how it works
# A while loop in Python is used for executing a block of code repeatedly as long as a specified condition
# is True. It works by evaluating the condition before each iteration. If the condition is True, the loop continues;
# if the condition becomes False, the loop stops executing.


# SECTION 2: FOR LOOPS
# Example of a for loop
list_name = [1,2,3,4,5]
for variable_name in list_name:
  print(variable_name)

# Write a for loop that prints numbers from 1 to 5 (inclusive)
for num in range(1, 6):
  print(num)


# Write a for loop that iterates over the following list of strings and prints each fruit
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)


# Write a for loop that iterates over the following list and prints only even numbers
nums = [4, 5, 7, 8, 10]
for num in nums:
  if num % 2 == 0:
    print(num)


# SECTION 3: WHILE LOOPS

# Write a while loop that prints numbers from 1 to 10 (inclusive)
num = 1
while num <= 10:
  print(num)
  num += 1


# Write a while loop that calculates the sum of numbers from 1 to 10
num = 1
total = 0
while num <= 10:
  total += num
  num += 1
print(total)


# Write a while loop that calculates the sum of only the even numbers from 1 to 10
num = 1
total = 0
while num <= 10:
  if num % 2 == 0:
    total += num
  num += 1
print(total)


# Write a while loop that prints elements from the following list:
rick_strings = ["never", "gonna", "give", "you", "up"]
index = 0
while index < len(rick_strings):
  print(rick_strings[index])
  index += 1


# SECTION 4: CONTROL STATEMENTS

# Explain the purpose of the break statement in a loop
# The break statement is used to exit a loop prematurely, before its normal completion.
# When a break statement is encountered inside a loop, the loop is terminated immediately,
# and the program continues to execute the next statement after the loop.


# Explain the purpose of the continue statement in a loop
# The continue statement is used to skip the rest of the code inside a loop for the current iteration and
# move on to the next iteration of the loop. When a continue statement is encountered, the loop's control
# jumps to the next iteration without executing the subsequent code within the loop for the current iteration.


# Using rick_strings, write a while loop that prints elements before "you"
index = 0
while index < len(rick_strings):
  if rick_strings[index] == "you":
    break
  print(rick_strings[index])
  index += 1


# SECTION 5: NESTED LOOPS

# Write a nested for loop that prints a pattern of stars (*) in the shape of a right triangle. For example:
# *
# * *
# * * *
# * * * *
# * * * * *
# Hint: print("\n") will print a new line
for i in range(1, 6):
  for j in range(i):
    print("* ")
  print("\n")

# Using the list of suits and the list of ranks, populate the deck with strings of every combination of suits and ranks list using a nested for loop

# deck should be ["Ace Hearts", "2 Hearts", "3 Hearts"...]

suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
deck = []

for s in suits:
  for r in ranks:
    deck.append(r + " " + s)