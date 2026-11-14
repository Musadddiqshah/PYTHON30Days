#  Lot of string Methods They Use for diffrent type of activities
#  Allll Methods Return New String They Never Change old One Because String Are Immutable Unchangable.
text = "I love Python"
print(text.upper())  # Convert All Letters to Upper Case and Return a New String. That never change old One Because strings are Immutable. Even When you do print(text) that Give you orignal Unchanged string.
print(text.lower())  # Convert All Letters to Lower Case
name = "musaddiq shah "
print(name.capitalize()) # Musaddiq shah. that Do Capitalize Sitring
# print(name)  # That Give you Old String Unchanged Because String Not Changable
text = "  Hello World  " # Look How Many Spaces Around string remove it using strip() method
print(text) # that Return With Spaces
print(text.strip()) # that Remove extra Spaces

text = "I Love Python"
#
print("Lenght of text",len(text)) # len = length
print(text.find("Python"))# 7 beause Python Indexed on 7. Remmeber In Python Counting Starts from 01.
print(text.replace("Python", "Coding")) # Return I Love Coding
print(text.count("o")) # Return 2 In text we have 2 ( o )
text = "Hello world! 123"
print(text.startswith("H")) # True Because start with Hello So H is Hello
print(text.endswith("world")) # False because end on 123 not world
print(text.isdigit()) # Because not digits these are texts
print("123".isdigit()) # because these are digits
# Check More Methods on Python site python.org
friends = "Mutee, Faheem, Naseem, Yaseen,"
print(friends.split()) # Convert str to list.
#   in, not in. Check Substring
print("A" in "SHAH") # True Because A in SHAH.
print("fawaz" in "Fawaz is Good Boy") # False Because in string we have Fawaz not fawaz lower case.
#   Python is Case-Sensitive.
print("love" not in "I Love Python") # True because lower case love not in I Love Python
