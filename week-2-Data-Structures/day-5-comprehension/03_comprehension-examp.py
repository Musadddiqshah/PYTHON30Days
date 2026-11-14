#  Real Examples of Comprehension
# word count from a list and return in list
words = ["Musaddiq","Yaseen","Faheem","Mutee","Naseem"]
count = [len(word) for word in words]
print(count)
# same example, but return a word also with length
count = {word: len(word) for word in words} # This is better
print(count)
# Example 2. Combine two lists
menu = ["Coffee","Tea","Biscuit"]
prices = [50,30,60]
combine = {item: price for item,price in zip(menu,prices)}
print(combine)

# if You Dont Know About zip()  func you need To Learn This Look  at Last Lines of this file

# Example 3. Names with index
names = ["Musaddiq","Yaseen","Faheem","Mutee","Naseem"]
indexed = {index:name for index , name in enumerate(names,start=1)} # already learned about enumerate()  that Return with index, start=1 mean start from 1 otherwise index start from 0
print(indexed)
# Example 4. Pass/Fail Label
names = {"Musaddiq":68,"Yaseen":52,"Faheem":47,"Mutee":89,"Naseem":45}
results = {name: "Pass" if score >= 50 else "Fail" for name, score in names.items()}
print(results)
# Output is:
"""
{'Musaddiq': 'Pass', 'Yaseen': 'Pass', 'Faheem': 'Fail', 'Mutee': 'Pass', 'Naseem': 'Fail'}
"""
# Example 5. lable even odd
numbers = [17,29,42,11,192,107,58]
lable = {num:"even" if num % 2 == 0 else "odd" for num in numbers}
print(lable) # Output is:
"""
{17: 'odd', 29: 'odd', 42: 'even', 11: 'odd', 192: 'even', 107: 'odd', 58: 'even'}
"""












# ===== What is zip()? =====
# zip() is a built-in function that PAIRS items from two (or more) lists
# by their position — like a zipper on clothes.
#
# Example:
#   menu   = ["Coffee", "Tea", "Biscuit"]
#   prices = [50,       30,    60]
#   zip(menu, prices) → pairs them up:
#       ("Coffee", 50)
#       ("Tea",    30)
#       ("Biscuit",60)
#
# ⚠️ zip() returns a "zip object" — NOT a readable list.
#    To see it:   list(zip(a, b))
#
# ⚠️ zip() stops at the SHORTER list — extra items are ignored:
#    zip([1,2,3,4], ['x','y'])  →  [(1,'x'), (2,'y')]   (3, 4 dropped)
#
# ===== How to use zip() with dict comprehension =====
#   {key: value for key, value in zip(list1, list2)}
#
# The pair from zip() UNPACKS into two variables (key, value).
# No loop is written by you — the comprehension does it.
#
# ===== Shortcut =====
#   dict(zip(list1, list2))   ← same result, shorter
#
# ===== Real uses =====
#   - Two lists → one dict            (menu + prices → menu_dict)
#   - Combine student names + marks   (names + marks → report)
#   - Add filter:  if price < 55
#   - Add ternary: "cheap" if price < 55 else "expensive"




