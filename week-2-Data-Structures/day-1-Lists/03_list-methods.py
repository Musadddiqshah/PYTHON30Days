# Python Provides built-in Methods Thats operates on Lists. For Example append method is Use to add new Element at The End of list.
# 1. append --- Add Item At the End
# Lets do it Practically.
friends = ["Yaseen","Mutee","Faheem"]
friends.append("Naseem") # That Add Naseem At The End Of List
print(friends)
#  Output Will Look Like This       ['Yaseen', 'Mutee', 'Faheem', 'Naseem']
#.          
# 2. extend() Add More Items at The end But extend Take Argument Like You Need To Give it New Items With Brakets Like Give It listname.extend(["Item"]) Thats Add More Items At The End
# Lets Do It Practically
fruit = ["Apple"]
fruit.extend(["Banana","Mango","Orange"]) # If You give it arguments without brackets [ ] that  give You Error.!!!
print(fruit)
# Another Easy Way To use Extend First We Make Another List That Contain Items Then We use extend to add These on Out list.

lst1 = ["cat"]
lst2 = ["dog","Bird"] # We are Add these on end Of lst1
lst1.extend(lst2)
print(lst1) # Shows ['cat', 'dog', 'Bird'].

# 3. sort method  ---- sort items from low to high lets do it

alphabets = ["C","F","A","D","E","B"]
alphabets.sort()
print(alphabets)
# that Sort All To Make It From Low to High.
# We Have A List Name friends Now Will Sort it to make it best.
friends = ["Yaseen","Mutee","Faheem","Farhan","Aadil","Waseem","Zaheer","Husain","Ibrar","Saad","Noman","Ikram","Naseem","Ismail","Tanveer","Imran","AmanUllah","Aftab","Munir","Nazeer","Javed","Hidayat","Musawwer","Ameen","Shahzaib","Ataa","Israr","Saqib","Shoib","Shafeeq"]
print(len(friends))
friends.sort()
print(friends) # Now We Have Sorted Names Of friends.
# You are Thinking I have Lot of Friends But In Reality That Was Totally = False.
#
# 3. insert add Item On Index/Position where you need to add.
# Work Like This insert(inde,,"item")
lst = ["cat","bird","dow"]
#index  0       1     2
lst.insert(1,"dog") # Output:     ['cat', 'dog', 'bird', 'dow'].
print(lst)
 # Add Item On index Put That Current Item To right. Add New item To Index Of old.

# 4.  Remove Items (three Ways)
# remove method. -- remove first matching item
fruits = ["Apple","Banana","Mango","Banana"]
print(fruits) # Show full list
# Now We Remove Banana
fruits.remove("Banana")# That Remove First Banana Not All. Mean remove() method is used remove first matching item from list.
print(fruits) # Only one Banana in results.
# If item not exists in List So If You wan’t to remove item that Not exist in List You will get ValueError !!!!!!
# fruits.remove("Orange") # Error !!!!!!!
# print(fruits) # ValueError Because item ("Orange") not exists in fruits.
# So Be Aware If you mistake spell you will get Error of this type.......
#
# 5. pop method --- remove by position. I Mean Remove By Index. Formula: list.pop(index)
lst = ["Python","Java","C++","C#","C","JavaScript"]
lst.pop(5) # That Remove JavaScript from lst.
print(lst)
# lst.pop(9) # We are Saying Remove the Value On Index 9. so That Return Index Error !!!  Because that index is not exists.
# -----
#   --- del remove by index or slice. I Mean Remove More Items Not Just One.
lst = ["Python","Java","C++","C#","C","JavaScript"]
del lst[1] # Remove Java From lst
print(lst)
# Remove By Slice The Real Power.
lst = ["Python","Java","C++","C#","C","Bash"]
del lst[0:4] # Remove From zero to 3. last is Not Encluded Because we alredy learn About it last is not encluded.
print(lst) # ['C','Bash']

#. 7. clear() method remove Alll Clear List Full
lst = ["Python","Java","C++","C#","C","JavaScript"]
lst.clear()
print("Noting Will Print here >>> because cleared >>",lst)

# 8. index method. find the first matching item and return index.


lst = ["Python","Java","C++","C#","C","JavaScript"]
print(lst.index("Python")) # Return 0 beacuse Python Is Located on 0 index. if index Not Found Like print(lst.index("php")) so tHat was not in out list That Guve You ValueError !!!!!!!!!  Error.
#
# 9. count method -- count how many mathing items in list like this count("item")
lst = ["Python","Java","C++","C#","C","Python"]
print(lst.count("Python")) #  return 2 beacuse 2 (Python) name item in lst.
# If Nothing That Return 0..


# Check if item exists.
lst = ["Python","Php","C++","C#","C","Swift"]
print('Java' in lst) # False Because No Java Item in lst .
print('php' in lst) # False. Wyyyy Becasue in lst we Have Capitalize Php  not 'php' in small Case Remember Python is Case Sensitive Language.
print('Php' in lst) # True Because We have Php in Our List.

# 10. reverse method --- reverse whole List.
lst = ["Python","Php","C++","C#","C","Swift"]
lst.reverse()
print(lst) # Now We Have a List Start from End. You Can Use also in Slicing Like.
lst = ["Python","Php","C++","C#","C","Swift"]
print(lst[::-1]) # same That Make Reverse List . and and Stirng also.
# <.......Both Are  same Thing.......>

# Copying A list
list_1 = ["Python","Php","C++","C#","C","Swift"]
list_2 = list_1
print(list_2)
 # I Think You are Thinking About This Trick But You Can Use a copy() method. Like This.
list_1 = ["Python","Php","C++","C#","C","Swift"]
list_2 = list_1.copy() # U can also use slice trick Like This.. list_2 = list_1[:] same As Like This
print(list_2)

# Loooooop On List Already You know. Like this.
list_1 = ["Python","Php","C++","C#","C","Swift"]
for item in list_1:
    print(item)

# Use With enumrate() Also print index of items 
list_1 = ["Python","Php","C++","C#","C","Swift"]

for i, item in enumerate(list_1):
    print(i,item)
#  ----- Output Looks Like This items with indexes
'''
0 Python
1 Php
2 C++
3 C#
4 C
5 Swift
'''
# Basicly enumerate() is a method used in Loops that return index of items .


# Joining Two Lists. (Already Learned)
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = list1 + list2
print(list1 + list2) # 

# Repeatation Of List....

lst = ["Musaddiq","Yaseen"]
print(lst * 3) # Repeat Items to 3 times.

# Convertion between list and String
# List to String
lst = ['Musaddiq Shah',"Yaseen Shah",]
print(" ".join(lst)) # Ruuuuule: Must be alll str for joining...
print(','.join(lst))
print('-'.join(lst))

# String to List

string = "Musaddiq Yaseen"
print(list(string)) # that make every character to list Type Check Output Also......
# Best And Easy Use split method of strings...
fruits = "Apple Mango Orange Banana"
lst = fruits.split()
print(lst) # This output will Shock You Because That Gave what we want.

# range() to List. we alredy known about range() funtion is creating rang between Number that Default start from 0 and end number is Not encluded like if you want 1 to 10 you need to give it 1 to 11 lets use in list

lst = list(range(1,11))
print(lst) # best Ways to add Number in lists...
# Find Min Max... use builtin funtion Like min max these are not list method But best to use it.....
numbers = [8, 9, 3, 4, 1, 6, 7, 2, 5, 10]
print(min(numbers)) # Find Lowest in list..
print(max(numbers)) # Return biggest in List...
print(sum(numbers)) # Return Addition Of Allll Tga Was Built-in functions Not list Methods.......

names = ["AM Musaddiq","Yaseen Shah","Mutee Ullah"]
print(max(names)) # Largest... Srart from A .......
print(min(names)) # lowest Z....




