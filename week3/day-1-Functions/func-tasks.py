# 1. write a function called multiply that multiply 2 given numbers.
def multiply(num1, num2):
    return num1 * num2


print(multiply(2, 4))  # that mean 2 * 4 = 8


# 2. write a function called greeting Hello to given name as parameter
def greet(name):
    return f"Hello {name}"


print(greet("Musaddiq"))  # Output is Hello Musaddiq

# 3. write a function called check_num(num) that return Negative Positive and Zero On given number


def check_num(num):
    if num > 0:
        return f"{num} is Positive"
    elif num < 0:
        return f"{num} is Negative"
    else:
        return f"{num} is Zero"


print(check_num(-6))


# 4. Write a function called introduce(name,age,city): that return sentenct like "My name is Farhan i am 18 years old from Nushki"
def introduce(name, age, city):
    return f"My name is {name}, i am {age} years old from {city}"


print(introduce("Musaddiq", 19, "Nushki"))
# call it 3 ways like All Position: ("Musaddiq",19,"Nushki"). All Keywords: (name="Musaddiq",age=19,city="Nushki"). Mixed likde (name="Musaddiq",18,city="Nushki")
print(
    introduce("Yaseen", age=16, city="Ahmed Wal")
)  # Keyword argument come after Positional Argument. This is Tricky you need to practice it more than 5 times in a day.


# 5. write a function called total(*nums) that take numbers as arguments from user and return sum of all numbers.
def total(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(total(1, 2, 3, 4))  # return 10 this mean 1+2+3+4 = 10
print(total(5))
print(total(0))


# Another Way to make this easy:
def easy_total(*nums):
    total = sum(
        nums
    )  # sum is bultin function for sum numbers usage sum(1,2) output is 3
    return total


print(easy_total(1, 2, 3, 4))
