#  We Learn About Comparision Opreaters in DAY3. You Can Check it. ==,>=,<=,>,<,!= Alredy Learned About These if you Know You Know.
x = 10
if x == 10:
    print("Ten")
elif x > 5:
    print("Big")
elif x != 20:
    print("Not Twenty")

#   Logical Operaters. We Alredy Learned About That. and, or, not
# and = Return True if both are true
# or =  return True if at least one is true
# not = reverse True = Flase. False= True
age = 21
has_id = True
if age >= 18 and has_id: # Return True and print next. because both conditions are True
    print("You can Enter")
else:
    print("You can't Enter")

age = 11
has_id = True
if age >= 18 and has_id: # Return False because one condition is False. (and) operaters need both condition are True.
    print("You can Enter")
else:
    print("You can't Enter")

