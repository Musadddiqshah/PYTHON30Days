# Real Use of Function.
# Example 1. Greet      -- basic
def greet(name):
    return f"Hello {name}"


print(greet("Musaddiq"))


# Example 2. Add       -- basic
def add(num1, num2):
    return num1 + num2


print(add(20, 30))


# Exampls 3. Power Number -- basic
def power(num):
    return num**num


print(power(3))  # mean 3*3*3 = 27


# Example 4. Even or Odd -- basic
def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check(4))  # Even
print(check(5))  # Odd


# Example 5. sum a list  -- A-basic
def sum_list(lst):
    result = 0
    for num in lst:
        result += num
    return result


print(sum_list([1, 2, 3, 4, 5]))  # 15
print(sum_list([191, 299, 16, 287, 129, 78]))  # 1000


# Example 6. count vowels.  - advance
def count_vowels(word):
    count = 0
    vowels = ""
    for ch in word.lower():
        if ch in "aeiou":
            count += 1
            vowels += ch
    return f"{count} vowels in '{word}' vowels are '{vowels}'"


print(
    count_vowels("Hello World")
)  # Output is: 3 vowels in 'Hello World' vowels are 'eoo'
print(count_vowels("Musaddiq"))  # output is: 3 vowels in 'Musaddiq' vowels are 'uai'
