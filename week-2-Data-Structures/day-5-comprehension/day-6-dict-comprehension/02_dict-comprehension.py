# dict comorehension - same idea but for a dict.
# starting with a loop
squares = {}
for i in range(1, 6):
    squares[i] = i * i
print(squares)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# with comprehension
# we use {} curley brackets for dicts
squares = {i: i * i for i in range(1,6)}
## i:  <==== mean take " i " as key. i * i mean use value as key * key like if key is 1 so that use value as i * i = 1.
print(squares)
# some examples
# length of words
words = ['Yaseen','Musaddiq','Farhan','Naseem']
length = {word: len(word) for word in words}
print(length)
# in same example if we use manual loop We will do this
length = {} # storing words and there length
for word in words:
    length[word] = len(word)
print(length) # return same results
# Example 2. swap key,value
orignal = {1:'one',2:'two',3:'three'}
results = {}
for key,value in orignal.items():
    results[value] = key
print(results)
# Do same with comprehension
orignal = {1:'one',2:'two',3:'three'}
results = {value: key for key, value in orignal.items()}
print(results) # same results but shorter and   faster.
# With if statement. same as list use if only on last
# get only scores higher than 60
players = {'Yaseen':47,'Faheem':53,'Mutee':74,'Naseem':68,'Musaddiq':83}
results = {name: score for name,score in players.items() if score >= 60}
print(results)
# With else. same as list with else we use  statements on first.
results = {name: 'Pass' if score >= 60 else 'Fail' for name,score in players.items()}
print(results) # Output is {'Yaseen': 'Fail', 'Faheem': 'Fail', 'Mutee': 'Pass', 'Naseem': 'Pass', 'Musaddiq': 'Pass'}
# Remember no elif in comprehension - use nested else if needed
# Why not use dict Comprehension
'''
dict comprehension is great when it short. if it become hard to read use loop instead.
'''
# Written By Musaddiq Shah. Date: Nov 10 2026





