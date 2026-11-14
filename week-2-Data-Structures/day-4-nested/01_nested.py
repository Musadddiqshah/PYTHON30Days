# 1. What is nested data?
# Nested data means data inside data — list in list, dict in dict,
# list in dict, tuple in dict, anything mixed. Think: boxes inside boxes.

# 2. Why nested data?
# Real-world data is rarely flat:
#   - A classroom has students; each student has subjects; each subject has marks.
#   - A JSON API response: user → address → coordinates.
#   - A shopping cart: items → price, quantity, discount.

print("\n=== Nested List ===\n")

# ---------- 2D list / matrix ----------
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(numbers, type(numbers))       # [[1,2,3],[4,5,6],[7,8,9]] <class 'list'>
print(numbers[0])                   # [1, 2, 3]
print(numbers[0][0])                # 1 — numbers[row][col]

# Loop over nested list
for row in numbers:
    print(row)

# Loop over every element
for row in numbers:
    for column in row:
        print(column, end=" ")
    print()

# Change an element
friends = [
    ["Yaseen", "Farhan", "Aamir"],
    ["Faheem", "Naseem", "Mutee"],
    ["Zaheer", "Ibrar", "Husain"],
]
friends[0][1] = "Farhan Khan"
print(friends)

# Sum each row
for row in numbers:
    print(sum(row))     # sum([iterable]) → total. sum(1, 2) is WRONG.

# ---------- Nested dict ----------
students = {
    "Yaseen":  {"age": 15, "marks": 729, "city": "AhmedWal"},
    "Farhan":  {"age": 18, "marks": 459, "city": "Nushki"},
    "Naseem":  {"age": 20, "marks": 220, "city": "Quetta"},
}
print(students["Yaseen"]["city"])    # AhmedWal

for name, info in students.items():
    print(f"\nname: {name}")
    for key, value in info.items():
        print(f"    {key}: {value}")

# ---------- Dict inside list (records) ----------
print("\n\tDict inside List\n")

students = [
    {"name": "Yaseen",   "age": 14, "marks": 59},
    {"name": "Musaddiq", "age": 18, "marks": 63},
    {"name": "Faheem",   "age": 19, "marks": 53},
    {"name": "Mutee",    "age": 21, "marks": 73},
]
print(students[0]["name"])
print(students[-1]["name"])

for student in students:
    print(f"Student: {student['name']} is {student['age']} years old, marks {student['marks']}")

for i, student in enumerate(students, start=1):
    print(f"{i}: {student['name']} — {student['marks']}")

# ---------- List inside dict ----------
person = {
    "name": "Musaddiq Shah",
    "age": 18,
    "city": "Nushki",
    "skills": ["Python", "Html", "Css", "Java"],
}
print(person["skills"])
print(person["skills"][0])
print(person["skills"][-2])

# Loop over the list inside the dict
classroom = {
    "teacher": "Musaddiq",
    "students": ["Mutee", "Yaseen", "Naseem", "Faheem"],
    "marks":    [50, 39, 70, 93],
}
for student in classroom["students"]:
    print(student)

# Loop two lists together with zip()
for name, marks in zip(classroom["students"], classroom["marks"]):
    print(f"{name}: {marks}")

# zip with index
for i, (name, marks) in enumerate(zip(classroom["students"], classroom["marks"]), 1):
    print(f"{i}. {name}: {marks}")

# End — AM Musaddiq · 5-11-2026 · AhmedWal, Nushki, Balochistan, Pakistan
