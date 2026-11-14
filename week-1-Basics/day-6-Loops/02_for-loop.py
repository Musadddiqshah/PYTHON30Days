# for loop. Mean repeat for know number Like you will see now.
number = 11
for i in range(number):
    print("Hello World!")

# What actually range() is. so bacicly range is a built-in function for printing number as given range. range also start from zero and end is not encluded.
# Forms of range()
# range(5) # from zero to 4 bcz end is not encluded
# range(0,5) # from zero to 4 same.
# range(7,20) # from 7 to 19.(20 = end was not encluded)
# range(0,10,2) # from 0 to 10 and step 2 mean skip every 2. output is 2,4,6,8.
# range(10,0,-1)  = reverse# from 10 to 0 and step -1 basiclly that give reverse numbers.
# One Rule. STOP IS NOT ENCLUDED

# Loop Over String.

for i in "Musaddiq":
    print(i)
# Output
'''
M
u
s
a
d
d
i
q
'''
# Sum with loop very commom pattern -- accumulate


total = 0  # we will take a variable empty.
for number in range(5):
    total += number # add every number to total and assing it to total variable u can use this total = total + number. first that add 1 then add + 2 then add +3 then +4. and stop because end is not encluded, 1+2+3+4 = 10
print(total)

# Example 2 Mutiplication Table one of the best Exersice Learn it.

# We need Mutiplication Table of 10
number = 10
for i in range(1,11): # 11 because end is not encluded so 1 to 10
    print(f"{number} X {i} = {number * i}")
# Mutiply from 1 to 10 every number to number

#  Nested Loops. Loop inside Loop

for i in range(3):
    for j in range(3):
        print("HeLLo World") # Total run = 3 * 3 = 9 . Rule inner loop Finish fully for each outer loop step.
