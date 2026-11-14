#  01. What is list Comprehension. ?
# Short way to make a list with one line of code

# Normal Way Loop and Append

numbers = []
for i in range(1,11):
    numbers.append(i)
print(numbers)
# That Add from 1 to 10 to numbers - list
# Using comprehension 
numbers = [i for i in range(1,11)] # Same Results But Shorter, Much Faster Than Manual loop.
print(numbers)
# Basic Syntax
# [Expression for item in iterable]
# Mean of this:
"""
Expression -- what you want in list
item -- each value
iterable -- range,list,str,set().

In Simple Language: Make a List of Expression for each item in iterable.
"""
# Simple Exampls. Squares
squares = [n * n for n in range(1,6)]
print(squares)
# Another. Double of each number in list
numbers = [1,2,3,4,5]
double = [n + n for n in numbers]
print(double) # Output must be [2, 4, 6, 8, 10]
# convert words to uppercase
words = ['yaseen','musaddiq','faheem','mutee','naseem']
upper = [word.upper() for word in words]
print(upper) # Convert all words to upper case
# Length of words
words = ['Yaseen','Musaddiq','Faheem','Mutee','Naseem']
# for word in words:
    # print(word,'Length: ',len(word))
# do same in comprehension
length = [len(word) for word in words]
print(length) # Look That's List comprehension That Return List you need to remember this.
# Using if condition on comprehension
print('==== Using if condition on comprehension =====')
evens = [n for n in range(1,11) if n % 2 == 0]
print(evens)
# Formula: [Expression for item in iterable if condition]
"""
Make a List of Expression for each item in iterables if condition is True
"""
""" With if else two choices
Put if else before for
"""
# Example Replace All Negative Numbers with 0
numbers = [1,2,-828,29.9,-29,-28,59,-1.9]
real = [num if num > 0 else 0 for num in numbers]
print(real)
# Example: Capitalize only names start with m or a for Better Highlight
names = ['musaddiq','asif','naseem','imran','farhan','amir','yaseen','faheem','abid']
highlights = [name.capitalize() if name.startswith('a') or name.startswith('m') else name for name in names]
print(highlights)
# Example convert full list name to reverse order
names = ['Musaddiq','Asif','Naseem','Imran','Farhan','Amir','Yaseen','Faheem','Abid']

reverse = [name[::-1] for name in names] # output: ['qiddasuM', 'fisA', 'meesaN', 'narmI', 'nahraF', 'rimA', 'neesaY', 'meehaF', 'dibA']
print(reverse)
'''
list comprehension is great when it short. if it become hard to read use loop instead.
'''


# Written By Musaddiq Shah. Date: Nov 10 2026
