print("  String Slicing ")
name = "Fawaz"
#     F a w a z
#     0 1 2 3 4
#    -5-4-3-2-1
# Work Like This [start:end]
#  start to End. Remember End is Not included..
print(name[0:3])  # Start from 0 to 3 (0,1,2) index. End Is Not Included and print name
print(name[:3])  # sams as like this Start from Zero index to 3 and Print it.
print(name[:]) # Mean Full String

print(name[-5:]) # That Gives Us from -5 to last So That Give Us Full string
print(name[-5:-2]) # that Gives us Faw

#    Slicing  With Step. Step = skip
# Formula:  [start:stop:step]

text = "Python"
print(text[0:6:2]) # Pto because that skip every 2
print(text[::2]) # same thing
print(text[::-1]) #  nohtyP. Return reverse of String Easy way to reverse 
#   Slice Mean We Need A Part Of string to print we can use slicing.
