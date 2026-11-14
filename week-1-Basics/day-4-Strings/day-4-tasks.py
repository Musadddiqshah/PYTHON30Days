#  1. take name from user as input that print uppercase and reverse of name.
name = input("Enter Your Name: ")
reverse = name[::-1]
print(reverse.upper())

#  2. Take sentence and print how many words inside Sentence. using split()
sentence = "My Name is Musaddiq Shah I am Live in Ahmedwal Nushki"

words = sentence.split() # first we convert string to list that make it like this ['My','Name'......] then we will print length
# print(type(words))
print(len(words),"Words in Sentence")

# 3. take a email adress from user then print domain afer @ (hint: find() slicing)

email = "aqsa733@gmail.com"
# print(email.find("@"))
print(email[8:])

# 4. Take a String and Replace all a to @ then print it
text = "aqsa"
print(text.replace("a","@")) # must be @qs@


#  Take a Sentence then define how many o in sentence

sentence = "A string is just text in Python. Words, sentences, letters — all strings. Strings in Python cannot be changed (immutable). Methods like .upper() return a new string — the original stays the same."
print(sentence.count("o")) # that count how many o is sentence






