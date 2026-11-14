# lambda — a small anonymous function without a name.
# Syntax:  lambda parameters: expression

square = lambda x: x * x
print(square(5))  # 25


# Same as:
def square_fn(num):
    return num * num


print(square_fn(5))  # 25


# When to use lambda: very short functions, especially inside
# sorted(), map(), filter().


# 1. Sort by the second item of a tuple
pairs = [(1, "b"), (3, "a"), (2, "c")]
pairs.sort(key=lambda x: x[1])  # sort by letter (index 1)
print(pairs)  # [(3, 'a'), (1, 'b'), (2, 'c')]


# 2. Sort dict by value (highest score first)
scores = {"Ali": 85, "Sara": 42, "John": 91}
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(sorted_scores)  # [('John', 91), ('Ali', 85), ('Sara', 42)]


# 3. filter() — keep only items where lambda returns True
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]


# 4. map() — transform every item
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8, 10, 12]


# ⚠️ But comprehensions can do the same, often clearer:
evens_comp = [x for x in nums if x % 2 == 0]  # instead of filter+lambda
doubled_comp = [x * 2 for x in nums]  # instead of map+lambda
print(evens_comp)  # [2, 4, 6]
print(doubled_comp)  # [2, 4, 6, 8, 10, 12]


# Rule of thumb:
#   - Use lambda mainly with sorted(key=...) when you need a custom order.
#   - For filtering / transforming, comprehensions are usually cleaner.
