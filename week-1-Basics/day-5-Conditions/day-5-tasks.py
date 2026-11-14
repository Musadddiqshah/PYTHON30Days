# 1. Take a Number input from user then print it Positive,Negative,or Zero Using Conditions

number = int(input("Enter Number: "))
if number == 0:
    print("Zero")
elif number < 0:
    print("Negative Number")
else:
    print("Positive Number")

# 2. Take a Number from user then print it even or odd
number = int(input("Enter Number: "))
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# 3. take age as input from user And print 0-12 Child, 13-19 teen, 20+ are Adult
age = int(input("Enter Age: "))
if age <= 12:
    print("You are Child")
elif age <=19:
    print("You are Teen")
else:
    print("You are Adult")

# 4. Take username and Password from user if Correct then print Welocome is Wrong then print Wrong Credentials.
print("====== Login Page ======")
username = input("Enter Username: ")
password = input("Enter Password: ")
if username == "aqsa" and password == "aqsa2235":
    print("Login Seccessfull")
else:
    print("Wrong Credentials. Retry")
