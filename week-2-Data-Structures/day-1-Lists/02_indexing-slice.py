# Indexing (Get One item) In List Same As String. Starts From Zero.
lst = ["Fawaz","Danish","Musaddiq"]
#        0        1          2
#        -3       -2         -1
print(lst) # Show Full Lst
print(lst[1]) # Show Danish
print(lst[0])# Show Fawaz
# print(lst[5]) # Index Error !!!¡ Any Elment Or Item That Not Exists in Lst If You Wan’t to access it You will Get index error.
lst[0] = "Fawaz Shah" # Changed.
lst[1] = "Dansih Shah" # Changed.
lst[2] = "Musaddiq Shah" # Changed.
print(lst)
# Negative Indexing
print(lst[-1]) # Musaddiq Shah
print(lst[-3])# Show Fawaz Shah


# Mutable = Can be Changed
# Immutable = Never Changed

# Remember List Are Mutable. And String Are Immutable

# Slicing in lits (Get Many Items)
# Same Formula Like String [start:stop] for step [start:stop:step]

fruits = ['Mango',"Grapes","Apple","Banana"]
#           0         1       2        3
#          -4         -3      -2      -1
print(fruits[0:3]) # ['Mango', 'Grapes', 'Apple'] end Is Not Encluded.
print(fruits[:]) # Full List
print(fruits[::-1]) # Reversed List
print(fruits[-4:-2])#['Mango', 'Grapes']

print(fruits[0:4:2]) # from start to end step/skip 2. ['Mango','Apple']
# We Alredy Know About Indexing Slicing In Strings Same Like List.

lst = ["Musadiq","Yaseen","Faheem","Mutee","Naseem"]
# We Can Modify A Slice. Of this list.
print(lst[1:4]) # Now We Change these To Others Names.
lst[1:4] = ["Ismail","Aadil","Farhan"]
print(lst)

# This Is Easy When You Practice It more than 20 Times On diffrent lists.
# On Nested Lists..
names = [['Musaddiq','Yaseen'],['Faheem','Mutee']]
print(names[0]) # Only Give First List.
print(names[0][0]) # Mean give use item on 0 index of first List.
print(names[1][::-1]) # Reverse Second List and Print it....


#   AM Musaddiq: From Nouski,Balochistan,Pakistan. Date 27.OCT.2026
