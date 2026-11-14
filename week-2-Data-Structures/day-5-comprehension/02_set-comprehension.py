# Same as list but. Remember No Dublicates in sets

numbers = {1,28,28,4,14,29}
unique = {n for n in numbers if n > 10}
print(type(unique),unique)
# The real Power of sets(). reemove dublicates
words = ['apple', 'banana', 'apple', 'kiwi', 'banana']
unique_words = {w for w in words}          # {'apple', 'banana', 'kiwi'}
print(unique_words)

# set Operations The Real Power makes sets specialize
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # union         → {1, 2, 3, 4, 5, 6}
print(a & b)    # intersection  → {3, 4}
print(a - b)    # difference    → {1, 2}
print(a ^ b)    # symmetric diff→ {1, 2, 5, 6}
""" Practical Use
students_day1 = {'Ali', 'Sara', 'John'}
students_day2 = {'Sara', 'John', 'Mia'}

both_days   = students_day1 & students_day2   # {'Sara', 'John'}
only_day1   = students_day1 - students_day2   # {'Ali'}
any_day     = students_day1 | students_day2   # all
"""
# if You are a Beginner You Can Easily Skip this That Not Needed Most. But Good To Know

# Written By Musaddiq Shah. Date: Nov 10 2026
