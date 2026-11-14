# Task 1. Print the even Number from 1 to 60. with while and for loop.
# a. With while loop
i = 1
while i < 61:
    if i % 2 ==0:
        print(i)
    i+=1 # make sure that inside of  while block not inside of if block

# b. with for loop.
for i in range(1,61):
    if i % 2 == 0:
        print(i)


# 2. Generate a Mutiplication table of given number by user
number = int(input("Enter Number: "))
for i in range(1,11):
    print(f"{number} X {i} = {number * i}")
# 3. Take sum of 1 to 10 use one loop
num = 0
for i in range(1,11):
    num += i # mean sum and assign number on every loop like add 1+2+3+4+5...
print(num)

# 4. take a Name of user and print it every letter on new line also print index of it

# Do This ↑

