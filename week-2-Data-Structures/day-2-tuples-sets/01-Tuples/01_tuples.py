 # What is Tuple...
 # A tuple is Like list But Can’t changed. Think Of its Sealed Glass Box you Can see inside But Can’t changed. Tuple are Make with Round Brackets ( ). Its Ordered Like List like That not change position of items Autmaticly. Īmmutable(Unchanged) You Can’t change tuple after creating It. Same As list Tuples Can Hold any DataType.

empty_tuple = () # This is Empty tuple
print(type(empty_tuple))

# Tuple with one item
a = ("Musaddiq") # This is string
b = ("Musaddiq",) # This is tuple.
# Remeber: If you need a One item tuple also add comma after item without comma you item is str or int like a = (1) is str but a = (1,) is a tuple. Don't Forget this This was Important.

names = ("Musaddiq","Yaseen")
print(type(names))
# names = ("Musaddiq") # This is string Not tuple If you want to add a Single item tuple use ('Musaddiq',)
# Rule: For one-item Tuple also ads Comma at the ensld of item.
  #comma  ( , ) <==  at end of items another Example: names = ('Musaddiq',) # so this is tuple Holding a Single items aslo in numbers use same num = (1) this is int. num = (1,) this is tuple..
numbers = (1,2,3,4)
print(type(numbers))

# Tuples Without brackets.

num = 1, # that Was a tuple
print(type(num))
name = 'Musaddiq',
print(type(name))
name = 'Musaddiq','Yaseen'
print(type(name))
num = 1,2,3,5,6 # that Was a tuple
print(type(num))



# Indexing And Slicing Same Like List.

names = ("Musaddiq","Yaseen","Mutee","Faheem","Naseem")
print(names[1]) # Indexing
print(names[-2]) # Negative indexing
print(names[0:3]) # Slicing
print(names[::-1]) # reverse .

# Same as List..
# But One Thing Remember tuple never cahnged .

# Loops  On Tuple
names = ("Musaddiq","Yaseen","Mutee","Faheem","Naseem")

for n in names:
    print(n)


# Tuple methods  Only two.
# count() index()
names = ("Musaddiq","Yaseen","Mutee","Faheem","Naseem",'Mutee')
print(names.index("Mutee")) # 2 Show Same that Show first Matching index.
print(names.count("Mutee")) # 2


# Tupels conatenation I mean Joining Of two tuples.

a = (1,2,3,4)
b = (5,6,7,8)
c = a + b # make new Tuple Not changed old
print(c) # Return New Tuple Orignal Unchanged Beacuse Of tuples are immutable(unchanged)

#  Tuple Unpacking === Very Useful. You Can unpack tuples into seprate variables.

nums = (1,2,3)
a,b,c = nums
print(a) # 1
print(b) # 2
print(c) # 3

# Using enumerate() on tuple In Lits That Return EACH ITEM AND HIS INDEX. IN TUPLE THAT RETURN SAME WITH TUPLE() So both are Same.
names = ("Musaddiq","Yaseen","Mutee","Faheem","Naseem",'Mutee')
for i, name in enumerate(names):
    print(i,name)



# End Of Tuple. It All Written By AM Musaddiq or Musaddiq Shah on Date Of 30,10,2026. On Fri Day.... Good Luck.
