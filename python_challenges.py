# imports
from functools import reduce



# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.
def sum_to(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total


# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
def largest(*nums):
    return max(nums)


# Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.
def occurances(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1


# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
def product(*nums):
    return reduce(lambda x,y: x * y, nums)

# 