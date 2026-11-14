#  F String is Best Way to Format String
name = "AM Musaddiq"
age = 18
# Without f-string
print("My Name is " + name + " My age is ",age)
# With f-string
print(f"My Name is {name} My age is {age}") # Easy And Beutiful.
#  Even You can Do Calculation in f-string
print(f"Sum of 2 + 2 = {2 + 2}")
print(f"Subtraction of 10 - 2 = {10 - 2}")
print(f"Mutiplicaton of 2 * 4 = {2 * 4}")
print(f"Division of 10 / 2 = {10 / 2}")


#   Extra On String
print("Apple" == "apple") # both are not same
print("banana" == "orange") # False Because banana is not aqual to orange
print("banana" > "apple")
print(len("banana") == len("orange")) # True Both are Have same length

#   Convert String To List.
text = "Love"
convert = list(text) # we cast str to list use type casiting
print(type(convert)) # Return List Because We converted to str to List
print(convert) # ['L', 'o', 'v', 'e']
