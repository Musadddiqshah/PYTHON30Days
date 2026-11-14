#  Lists. In Python are Collection of Mutiple Data Type in One 'Variable' like You can Add Any Datatype Item.

emptylist = []  # Empty List
print(type(emptylist)) # <class list>

fruits = ["Apple","Banana","Mango","Orange",12.7,12,True]
print(fruits)
print(type(fruits))
# Lists Are Collection of Mutiple Datatypes
# Lists are Ordered Like If you Put them in any Position That Return same position when print. simple  items keep their Position.
#
# Seprated By comma (,) [12,82,8]
# I mean These commas → , , , 
# Lists Are Made With Square Brackets [ ]
# Lists Are “ Mutable ” Like You Can Change Them Like This
books = ["Biology","English"]
print(books[0]) # That print biology Now we Need to Change Theme To Compute Make it Computer
books[0] = "Computer" # we are saying add Computer on Zero index in books Variable
print(books) # ['Computer', 'English']
# Strings Dont Allow This because strings are immutable
# string = "musaddiq"
# print(string[0]) # Show (m) we to convert it to  Caputal M
# string[0] = "M" # Error!! Because Strings Does Not Support Assignment One String Created Can’t changed. We Can Chage It By Creating New String Liek This
# print(string) We alredy Discussed About Stdings In Recent Week.

lst = ["Musaddiq","Yaseen"]
print(len(lst)) # Output is: 2. That Count items not characters Like strings
string = "Musaddiq Yaseen"
print(len(string)) # show 15 because that count every letter (M,u,s,a,d.....) in string but in List That Count only items.

#  List Concatenating ( + ). Joining Of Two Lists.
lst_1 = [1,2,3,4]
lst_2 = [5,6,7,8]
full_lst = lst_1 + lst_2
print(full_lst)

# Nested Lists List Inside List...

names = [['Musaddiq','Yaseen'],['Faheem','Mutee']]
print(names)
# Loop On List
friends = ["Musaddiq","Yaseen","Mutee","Farhan","Naseem","Faheem"]
for friend in friends:
    print(friend)
# Same Like String But That Give Every Element/item not Character Like String.


