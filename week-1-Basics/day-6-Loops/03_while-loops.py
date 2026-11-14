# While loop. REPEATS as Long as Condition is True

i = 0
while i < 11: # Loop when i less than 11 so that True that will run because that True.
    print(i)
    i+=1 # Very Very Important !!. Without this loop never end. Add and  Assign 1 to i on every loop
# Infinite Loop never End.
# i = 0
# while i < 11:
#     print(i)

# Never End You need to stop it Use Ctrl + c. Fix add i+=1 inside loop

# Real usage of while loop

attempt = 0
while attempt < 3:
    password = input('Enter Password: ')
    attempt +=1 # need password only three time this is use of while loop
# Another Example
word = ""
while word != 'quit':
    word = input('Type Something: ')
# That Keep asking for Word untill  u type quit to stop it.

i = 0
while i < 21:
    if i == 15:
        break # Loop breaks when 15 reached
    i+=1
print(i)

# else with loop

i = 1
while i < 6:
    print(i)
    i+=1
else:
    print("Finish")
 # Run else when loop is finished rearly used but good to know.
# Output:
# 1
# 2
# 3
# 4
# 5



