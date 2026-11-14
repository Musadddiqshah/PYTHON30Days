# Day 6 Mini Project Guessing Game.
# A complete beginner Friendly Project from ( int ,input, if ,elif ,else ,for ,while ,break, continue ,f-string) anything Else You Learned
# What this Game does.
# Computer Pick a Random number from 1 to 100
# Player Guess it
'''
# Program/Computer says:

too low : Guess Higher
too high : Guess lower
correct = win
Count how many times you tried .
ask for play again
'''
# Step 1 learn random. random is a built-in python Module called random.
# import random   # import random module in our program now we can use it.
# number = random.randint(1,100) # we say random pick random number from 1 to 100.
# print(number) # run it few times then you get random numbers

#  Step 2. before write code See the Full sketch of code.
'''
1. import random
2. pick secret number from 1-100
3. set tries = 0
4. loop:
    a.ask user for guess
    b.convert to int
    c.tries+=1
    d.if guess < secret print "too low"
    c.elif guess > secret print "too high"
    d.else: print correct and loop break.
5. print total tries

'''
# Version 1. Basic Game

import random # bring the module

secret = random.randint(1,100) # pick a random number from 1 to 100

tries = 0 # Varible that Value is 0
print("Guess A Number From 1 to 100")
while True: #  loop Forever
    guess = int(input("Enter The Number: ")) # take a number from user
    tries += 1
    if guess < 1 or guess > 100:
        print("Enter Number between 1 to 100")
    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print("Correct You Won")
        break # When User guess that correcr break that loop
print("You are tried ", tries , " times") # when loops break that That Show tries

