# Find Biggest In List..
numbers = [12, 82, 152, 222, 292, 362]
big = numbers[0] # Take a first as variable.
for num in numbers:
    if(num > big):
        big = num # When Loop run That Add Every item of list in big variable Every Times Loop Run That Also Check Can num is big than 'big' variable.
print(big) # return biggest from list.
# we can use this simple print(max(numbers))
# Remove Dublicates ...

languages = ['Java','C#','Python','Bash','Php','JavaScript','Python','C++','C#','Php'] # We have three³ dublicates now we are Removing theme using a List......
unique = [ ] # We are Adding All Uniqes In This list....
for language in languages:
    if language not in unique:
        unique.append(language)
print(unique) # Now That Return Only Unique names No Dublicates...

# Names List That Aks For Names You Can add It That Print it..
names = []
print('+== Add 5 Names ==+ ')
for i in range(1,6):
    name = input('Enter Name: ')
    names.append(name)
print(f'Your have {len(names)} names: {names}')


#  Check Google Or AI for More Examples......
