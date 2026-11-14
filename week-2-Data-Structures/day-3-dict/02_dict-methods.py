# dict methods..
friend = {
        'name':'Musaddiq',
        'age': 18,
        'class':'Twelfth',
        'city':'Ahmed Wal'
        }
#  1.  get(). get value of given key.
print(friend.get('name')) # Return Musaddiq
print(friend['name'])# U can use this but when key is not found that return error.
# print(friend['Country']) # Return Error because No key name Country
# But u can escape from error use get() method.
print(friend.get('Country')) # Return None because not found this key.
# So You Learned get() method is used for get value of given item.

# 2. changing and adding New item. you can only change values in list not keys.
friend = {
        'name':'Musaddiq',
        'age': 18,
        'class':'Twelfth',
        'city':'Ahmed Wal'
        }
# Changing
friend['name'] = 'Musaddiq Shah' # we can use directly name of item for changing it value. Remember: Dictionaries are not indexed.
print(friend)
# Adding new item
friend['Country'] ='Pakistan' # That Add this key:value pair on the end of friend
print(friend)
# 2.1    update() method use for add More Items.
print("===========")
friend = {
        'name':'Musaddiq',
        'age': 18,
        'class':'Twelfth',
        'city':'Ahmed Wal'
        }

firend = friend.update({'age':19,'Country':'Pakistan'}) # We change age to 19 and Added New Item Name Country
print(friend) # Output is  {'name': 'Musaddiq', 'age': 19, 'class': 'Twelfth', 'city': 'Ahmed Wal', 'Country': 'Pakistan'}. This is Amazing.


# 3. pop() method remove key.
friend = {
        'name':'Musaddiq',
        'age': 18,
        'class':'Twelfth',
        'city':'Ahmed Wal'
        }
print(friend.pop('class')) # Remove key:value I mean Item named 'class'
print(friend)
# 4. popitem() remove all keep last pair. For more information go to python.org
friend = {
        'name':'Musaddiq',
        'age': 18,
        'class':'Twelfth',
        'city':'Ahmed Wal'
        }
print(friend.popitem())

# 5. del    mean delete item


friend = {
        'name':'Musaddiq',
        'age': 18,
        'class':'Twelfth',
        'city':'Ahmed Wal'
        }
del friend['class'] # Remove class key:value
print(friend)

# 6.  clear() allllll
friend = {
        'name':'Musaddiq',
        'age': 18,
        'class':'Twelfth',
        'city':'Ahmed Wal'
        }
print(friend.clear()) # Clear everything in dict and return None.

# 6.1 keys()  get all keys.

print(friend.keys()) # Return this  dict_keys(['name', 'age', 'class', 'city'])

# 6.2 values()   get alll Values in tuple
friend = {
        'name':'Musaddiq',
        'age': 18,
        'class':'Twelfth',
        'city':'Ahmed Wal'
        }
print(friend.values()) # Return this dict_values(['Musaddiq', 18, 'Twelfth', 'Ahmed Wal']) 
# 6.3  items()    Get all pairs
friend = {
        'name':'Musaddiq',
        'age': 18,
        'class':'Twelfth',
        'city':'Ahmed Wal'
        }
print(friend.items()) # Get alll Items so That Return This. dict_items([('name', 'Musaddiq'), ('age', 18), ('class', 'Twelfth'), ('city', 'Ahmed Wal')]). One Thing Is noticable These three methods (values,keys,items) are Returned In tuple format. Each Item is a Tuple

# 7  copy() .Copy a dictionary  I think You are Thinking This easy Way Use another Variable.
old = {"one":1,"two":2}
new = old
print(new) # I think you are Happy You are Copied it but !!!!
new['three'] = 3 # Added new item on old  dict name key is three and value is 3. What Happend When use a First variable I Mean
print(old) # WtF that show  {'one': 1, 'two': 2, 'three': 3} that mean that chnage our old dict But we are try to copying it. That Show This because This Same object Porblem That Whyy We used a copy() method
print('==== Using copy() Method')
old = {'one':1,'two':2}
# Use this for copy a Dict
new = a.copy()
new['three'] = 3
print(new) # {'one': 1, 'two': 2,'three':3}
print(old) # Now a is Untouched And Return This {'one': 1, 'two': 2}

# 8.   |   <====  (merge dictionaries)
friend = {'name':'Yaseen'}
age = {'age':'15'}
# print(friend | age) # U can Use this both are Same But This looks goood For reuse.
full= friend | age
print(full)


print('Writtten Byy  AM Musaddiq On  1-11-2026')
