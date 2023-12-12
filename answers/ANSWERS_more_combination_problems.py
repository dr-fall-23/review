# MORE COMBINATION PROBLEMS
'''
These problems will be a mix of many concepts you've learned so far, all mixed together.
This includes:
- Primitive data types (str, int, bool)
- Variables
- Conditional statements (if)
- Arrays
- Loops
- Functions
For each of the following problems, WRITE TESTS! 
'''


# Sum of Squares: 
# Write a function that takes an integer n as input and returns the sum of 
# the squares of all numbers from 1 to n.
def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i

# Test Cases
print(sum_of_squares(3))  # Output: 14 (1^2 + 2^2 + 3^2 = 14)
print(sum_of_squares(5))  # Output: 55 (1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55)


# Find Common Elements: 
# Write a function that takes two arrays as input and returns a new array 
# containing the common elements.
def find_common_elements(arr1, arr2):
    result = []
    for e1 in arr1:
        for e2 in arr2:
            if e1 == e2:
                result.append(e1)
    return result

# Test Cases
print(find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]
print(find_common_elements([10, 20, 30], [5, 10, 15, 20]))  # Output: [10, 20]


# Factorial: 
# Write a function that calculates the factorial of a given number.
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Test Cases
print(factorial(5))  # Output: 120 (5! = 5 x 4 x 3 x 2 x 1 = 120)
print(factorial(0))  # Output: 1 (0! is defined as 1)


# Array Span
# Write a function that takes in an array of integers, and returns the 
# difference between the largest number and smallest number in the array.
def array_span(arr):
    if arr == []:
        return 0
    max = arr[0]
    min = arr[0]
    for x in arr:
        if (x > max):
            max = x
        if (x < min):
            min = x
    return max - min


# Test Cases
print(array_span([1, 2, 3, 4, 5]))  # Output: 4 (5 - 1 = 4)
print(array_span([10, -3, 7, 20]))  # Output: 23 (20 - (-3) = 23)


# Threes Only: 
# Write a function that takes in an array of integers, and returns an array 
# containing only the integers divisible by 3.
def threes_only(arr):
    threes = []
    for x in arr:
        if (x % 3 == 0):
            threes.append(x)
    return threes

# Test Cases
print(threes_only([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: [3, 6, 9]
print(threes_only([30, 15, 9, 5, 12, 18]))  # Output: [30, 15, 9, 12, 18]