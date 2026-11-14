# Deep Nesting 3 or More Levels

school = {
    "name": "High School Ahmed Wal",
    "classes": {
        "9th": {
            "Teacher": "Ajmal",
            "students": [
                {"name": "Naseem Shah", "age": 17, "marks": 25},
                {"name": "Imran", "age": 16, "marks": 85},
                {"name": "Naqeeb", "age": 14, "marks": 35},
                {"name": "Qadeer", "age": 17, "marks": 61},
                {"name": "Uzair", "age": 16, "marks": 95},
            ],
        },
        "10th": {
            "Teacher": "Manzoor Ahmed",
            "students": [
                {"name": "Musaddiq Shah", "age": 17, "marks": 25},
                {"name": "Aadil", "age": 16, "marks": 85},
                {"name": "Aman", "age": 14, "marks": 35},
                {"name": "Fahad", "age": 17, "marks": 61},
                {"name": "Faheem Shah", "age": 16, "marks": 95},
            ],
        },
    },
}


print("School Name: ", school["name"])
print("9th Teacher Name: ", school["classes"]["9th"]["Teacher"])
print("10th Teacher Name: ", school["classes"]["10th"]["Teacher"])

# If You Understand Old Chapters That was easy for You.
print("\nMy Information\n ", school["classes"]["10th"]["students"][0])
print("\nMy Marks:", school["classes"]["10th"]["students"][0]["marks"])
# Ohhh My Marks Are Too Low I Want to increase it Like This
school["classes"]["10th"]["students"][0]["marks"] = 83
print("\nMy Updated Marks:", school["classes"]["10th"]["students"][0]["marks"])
# That was Easy Need Only One Time Focus On Code then you will never forget.
print("\nMy Marks", school["classes"]["10th"]["students"][0]["marks"])

# Adding New class, students or more ...

# school['classes']['11th'] = {
#         'Teacher': 'Ismail',
#         'students': [
#             {'name':'Yasir','age':19,'marks':57}
#             ]
# }
#  We Will Commented This That Only Used For Something To Learn
print("\n=== Loops On Deep Nested ===\n")
for class_name, classes in school.items():  # "name", "class"
    if not isinstance(classes, dict):
        continue  # skip "name": "High School..." I mean Strings
    for grade, info in classes.items():  # "9th", "10th"
        print(f"\n--- {grade} ---")
        print(f"Teacher: {info['Teacher']}")
        for student in info["students"]:  # list → iterate directly
            print(
                f"  {student['name']}: {student['marks']} marks, {student['age']} years old"
            )

# Another trick easy but tricky
print("\n ==== Another trick for loop deep nested ==== \n")
for grade in ["9th", "10th"]:
    students = school["classes"][grade]["students"]
    print(f"\n{grade} ({school['classes'][grade]['Teacher']})")
    for s in students:
        print(f"  {s['name']:} {s['marks']:}  age {s['age']}")
# if you not understand this Part You Can Skip it easily. if you want to understand then we will discussed this in next Days.

# Find Adults In Users

users = [
    {"name": "Musaddiq", "age": 19},
    {"name": "Yaseen", "age": 15},
    {"name": "Faheem", "age": 19},
    {"name": "Naseem", "age": 18},
    {"name": "Ismail", "age": 16},
    {"name": "Farhan", "age": 19},
    {"name": "Imran", "age": 15},
    {"name": "Mutee", "age": 22},
]

# Easy Way
for user in users:
    if user["age"] >= 18:
        print(user["name"], "is adult")
    else:
        print(user["name"], "is minor")


adults = [] # Adding Adults to this list
minors = [] # Adding minors to this list
for user in users:
    if user["age"] >= 18:
        adults.append(user["name"])
    else:
        minors.append(user["name"])

print("List Of Adults: ", adults)
print("List Of Minors: ", minors)

# Nested Data In Real Life - json
# Api Return Nested Data Like This
response = {
    "status": "ok",
    "data": {
        "users": [
            {"id": 1, "name": "Faheem", "address": {"city": "Nushki"}},
            {"id": 2, "name": "Naseem", "address": {"city": "Ahmed Wal"}},
            {"id": 3, "name": "Yaseen", "address": {"city": "Ahmed wal"}},
            {"id": 4, "name": "Mutee", "address": {"city": "Quetta"}},
            {"id": 5, "name": "Musaddiq", "address": {"city": "Ahmed wal"}}
        ]
    },
}

# Acces A City
print(response['data']['users'][0])
print(response['data']['users'][0]['address']['city'])

# Loop On All Users
for user in response['data']['users']:
    print(user['name'],"From ==>",user['address']['city'])

# searching a user name by id
users = {
    'Musaddiq': {'age':18, 'marks':49},
    'Faheem':  {'age':20, 'marks':43},
    'Yaseen':  {'age':15, 'marks':57},
    'Naseem':  {'age':19, 'marks':78},
    'Mutee':   {'age':20, 'marks':66}
}
# First Loop Check This
for name, info in users.items():
    print(f"Name: {name} | Age: {info['age']} | Marks: {info['marks']}")

# Search by name
search = input("Enter name: ")
if search in users:
    info = users[search]
    print(f"Age: {info['age']}, Marks: {info['marks']}")
else:
    print("User not found")

# Find Highest Marks In Dict

students = {
        'Yaseen':{'marks':526},
        'Musaddiq':{'marks':937},
        'Faheem':{'marks':276},
        'Naseem':{'marks':872},
        'Mutee':{'marks':529}
        }


check = students['Yaseen']['marks']
top = 0
winner_name = ''
for name, info in students.items():
    if(info['marks'] > check):
        top = info['marks']
        winner_name = name
print(f'Winner name: {winner_name} |','Marks: ',top)
# Output is: Winner name is Mutee Marks 937




