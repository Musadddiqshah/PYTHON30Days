# Real use of dictionaries (dict)

# 1.1  Student Record.
print("==-== Example 1 Studnet Record ==-== \n")
student = {
        'name':'Yaseen',
        'age':19,
        'class':'8th',
        'city':'Ahmedwal',
           }
print(student['name'])
print(student['age'])

# 1.2 Words and Urdu Meanings.
print("===-== Example 1.2 Words and Meanings ==-===\n")
words = {
        'mom':'Maa',
        'dad':'Baba',
        'go':'Jao',
        'come':'Aa jao',
        'who':'Kon',
        'his':'Wo',
        'love':'Pyar',
        'boy':'Larhka',
        'girl':'Larhki'
}
print(words['dad'])
print(words['mom'])
print(words['come'])
print(words['girl'])

# 1.3 Phonebook/contact
print('==-== Example 1.3 Phonebook ===-==\n')
phonebook = {
        'Musaddiq':"0369000000",
        'Yaseen':"0370672900",
        'Mutee':"0340000000",
        'Faheem':"0312345670",
        'Naseem':"034000000"
        }
print(phonebook['Musaddiq'])
print(phonebook['Mutee'])

# Example 2.1 Add And Upadte
print("==== Example 2.1 Add and update ====\n")
friend = {} # The empty dict.
friend['name'] = 'Yaseen'
friend['age'] = 15
print(friend)

# Using update() method On Here.
friend = {}
friend.update({"name":"Yaseen","age":15}) # This is Cool For Adding More items.
print(friend)

# Example 3.1 Loop And Print
print("====-== Loop and print ====\n")
student = {
        'name':'Musaddiq',
        'age':'18',
        'city':'Noushki',
        'class':'12th'
        }
for key,value in student.items():
    print(key,value)

# Another Example
data = {
        'Science':52,
        'English':69,
        'Biology':58,
        'Chemistry':39,
        'Math':21,
        'Urdu':95,
        'Physics':78
        }
for subject, marks in data.items():
    print(f'subject: {subject} marks: {marks}')
# This is best use if you Like.

# Example 3.2 loop nested.
students = {
        'Musaddiq': {'age':18,'marks':66},
        'Yaseen': {'age':15,'marks':73}
        }
for name,info in students.items():
    print(f'name: {name} - age: {info['age']} - marks:  {info["marks"]}')
# Woow Great Results if you see first time
print("\n^===^ Example 4 Find Highest Score ^===^ \n")
scores = {
        'Yaseen':49,
        'Naseem':56,
        'Faheem':41,
        'Mutee':77,
        'Musaddiq':46
        }
highest = 0
for name,score in scores.items():
    if score > highest:
        highest = score

print('Highest',highest)
# That Great Way To find highest.

# Example 4 == Count words from sententce.
print('\n==°°== Last Example Count words in sentence ===°°===\n')
sentence = "How are you my name is Musaddiq are you fine great  Musaddiq is you are fine"
words = sentence.split() # Converted to list

count = {} # empty dict for storing words.
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
# Amazing Practice it More Than Seven sentences.

"""
Dictionaries Are used everywhere.
Api Response
Json Data
Config setting
counting something
Database rows.  and more ......
"""





