# dict mean dictionary. A store of key:value pairs. think of its real doctionary that contain word as key and meaning as value like..
#   {'name':'Musaddiq', 'age':18}
empty = {}
print(type(empty))  # class dict not set. for set used empty = set().
friend = {"name": "Yaseen", "city": "Nushki", "age": 16}
print(friend, type(friend))
# In Here we have keys are‚ name,city,age, And itmes are, Yaseen,Nushki,16. work like this. simple
# {'name':'Yaseen'}
#   key :  value
# Each Item is a key:value
# Each item seprated by comma
# Made with curly braces
# Key Must be unique (no dublicates)
# Keys Must be immutable.
# Value can be anything.
# Mutable (changable)
# Orderd. keep Same as You  run it Not Change like sets
# =======================
# in here we have a empty dict now we add key:value to dictionary
name = {}  # we have empty dict
name["name"] = (
    "Musaddiq"  # we add key = name and value = Musaddiq. for adding items we use squre brackets.
)
print(name)
name["city"] = "Nushki"
print(name)
# print(name[0]) you can't access dict items with index because in lits indexing is not allowed You can Use key name directly
print(name["name"])  # Musaddiq , that Return value of name.
# print(name['age']) # Get keyError because no key associated with age  <== name. ======= if you want no errors use get() method of dicts. Key Not Exists Not a Problem no error
print(
    name.get("age")
)  # Return None. because no key exists Name 'age'. Rule use [] when key exists. Use get() when key Not exist.
num = {"one": 1, "two": 2, "three": 3, "four": 4}
num["five"] = 5  # That add this 'five': 5 at the and of
print(num)  #
# ==== In dictionary we can change a value using its keys Like this. But remember The keys Are immutable.

marks = {"Musaddiq": 90, "Yaseen": 92, "Faheem": 77}
# Now Will Change that Marks of Yaseen key.
marks["Yaseen"] = 100  # That change Yaseen marks from 92 to 100.
print(marks)

friend = {"name": "Yaseen", "age": 16, "city": "Nushki"}


print("name" in friend)  # True
print("Yaseen" in friend)  # False Because that only look for key in dict not values.. Only Check key exists or not. use This for keys.
print("Yaseen" in friend.values())  # Now That Return True Because we search in friend values. basically values() is method of dict that Return Value Liks this
friend = {"name": "Yaseen", "age": 16, "city": "Nushki"}
print(
    friend.values()
)  # That Retur all Value in this format   dict_values(['Yaseen', 16, 'Nushki'])
# Also You can use keys() method
print(
    friend.keys()
)  # Return all keys of dict. dict_keys(['name', 'age', 'city']) You Can change format using casting to list like this
print(list(friend.keys()))  # ['name', 'age', 'city'] Return in this list format.
# how to get all items {key:values}
print(
    friend.items()
)  # Return this dict_items([('name', 'Yaseen'), ('age', 16), ('city', 'Nushki')]) . Exersice Change it to list format.

# Loop On dictionaries.
marks = {"Yaseen": 50, "Faheem": 61, "Mutee": 73, "Musaddiq": 49, "Naseem": 53}
print(
    marks.items()
)  # In Here dict_items([('Yaseen', 50), ('Faheem', 61), ('Mutee', 73), ('Musaddiq', 49), ('Naseem', 53)]) we have Ever items in This format ('key',value).
for key, value in marks.items():
    print(key, value)  # Now You are thinking How That Work.

a = (("Musaddiq", 19), ("Farhan", 66))
# In here We have two items  and both have their own value. We have Tuple inside tuple we have 2 pairs
print(
    a, type(a)
)  # That Return (('Musaddiq', 19), ('Farhan', 66)) Type of Tuple. Do you remember we use tuple unpacking in recent day Now Same thing we will tried on here.
# Run Loop On here
a = (("Musaddiq", 19), ("Farhan", 66))
for i, k in a:
    print(i, k)
# OutPut is:
# Musaddiq 19
# Farhan 66
# We use this... for printing the Dict  keys and values.
# Tuple Unpacking === Very Useful. You Can unpack tuples into seprate variables.
# nums = (1,2,3)
# a,b,c = nums
# print(a) # 1
# print(b) # 2
# print(c) # 3

# ==== Nested Dictionary  dict inside dict ===#
students = {
        'Musaddiq': {'age':18,'marks':62},
        'Yaseen': {'age':16,'marks':70}
        }
print(students, type(students))
# Look for marks of Musaddiq
print(students['Musaddiq']['marks']) # 62
# Loop Through nested.
students = {
        'Musaddiq': {'age':18,'marks':62},
        'Yaseen': {'age':16,'marks':70},
        'Faheem': {'age':19,'marks':57},
        'Mutee': {'age':21,'marks':63}
        }
print(students)
for name, info in students.items():
    print(name,info['age'], 'year old','marks are',info['marks']) # If u not understand this read it run it.




