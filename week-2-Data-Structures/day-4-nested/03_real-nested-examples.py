# Example 1. Person Contact
contact = {
    'name': 'Ali',
    'phones': {
        'home': '0300-1234567',
        'work': '042-9876543'
    },
    'email': 'ali@example.com'
}

print(contact['name'])              # Ali
print(contact['phones']['work'])    # 042-9876543

# Example 2. A List of Stuudent and information of marks.
students = [
    {'name': 'Yaseen',   'marks': 526, 'class': 9},
    {'name': 'Musaddiq', 'marks': 937, 'class': 10},
    {'name': 'Faheem',   'marks': 276, 'class': 9},
]

for s in students:
    print(s['name'], s['marks'])

# A 3. school Dict of Dicts
school = {
    'class9': {
        'students': ['Yaseen', 'Faheem', 'Mutee'],
        'teacher': 'Mr. Khan'
    },
    'class10': {
        'students': ['Musaddiq', 'Naseem'],
        'teacher': 'Ms. Sana'
    }
}

print(school['class9']['teacher'])          # Mr. Khan
print(school['class10']['students'][0])     # Musaddiq

for cname, info in school.items():
    print(cname, '→', len(info['students']), 'students')

# Example 4.2
marks = {
    'Yaseen':   {'math': 80, 'english': 65},
    'Musaddiq': {'math': 92, 'english': 88},
}

print(marks['Musaddiq']['math'])    # 92

for name, subjects in marks.items():
    total = 0
    for sub, m in subjects.items():
        total += m
    print(name, 'total:', total)


# Example 5 A shopping Cart
cart = [
    {'item': 'pen',   'price': 20, 'tags': ['school', 'blue']},
    {'item': 'book',  'price': 300,'tags': ['school']},
]

total = 0
for p in cart:
    print(p['item'], '-', p['price'])
    total += p['price']

print('Total:', total)
print('First item tag:', cart[0]['tags'][0])   # school


# Example 6 Json Style Api
response = {
    'status': 'ok',
    'user': {
        'id': 42,
        'name': 'Ali',
        'friends': [
            {'name': 'Bilal', 'age': 20},
            {'name': 'Sara',  'age': 19},
        ]
    }
}

print(response['status'])                        # ok
print(response['user']['name'])                  # Ali

for f in response['user']['friends']:
    print(f['name'], f['age'])
