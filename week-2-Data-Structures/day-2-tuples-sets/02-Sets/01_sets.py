# What Is set(). Set is collection of items with No Duplicates, No Order, Not Indexed.
# Mutable (only add and remove, no change to existing items).
# Made with Curly brackets {}

# Empty set
empty_set = {}  # You might think this is a set — but it's a DICT (dictionary).
print(type(empty_set))  # returns dict

# ===== Correct way to create an empty set =====
empty_set = set()  # Now that is a set.
print(type(empty_set))

# Let's see set() looks ?
nums = {1, 3, 4, 5, 7, 1, 4, 8}
print(nums)  # that return output with removes duplicates,  {1, 3, 4, 5, 7, 8}

names = {'Yaseen', 'Mutee', 'Musaddiq'}
print(names)  # removes duplicates. NOTE: sets are ALWAYS unordered.
               # Order is never guaranteed and can change on every run.

num = {22, 7, 1, 6, 89}
print(num)  # small integers often LOOK sorted because Python hashes
            # small ints to themselves (hash(5) == 5). It is NOT a guarantee.
            # Never rely on set order — use sorted(my_set) if you need order.

# No indexing like list.
# names = {'Musaddiq', 'Yaseen', 'Mutee', 'Faheem'}
# print(names[0])  # TypeError: 'set' object is not subscriptable

#  Membership check is  (very fast unlike lists, ).
print(22 in num)   # True
print(99 in num)   # False

# The #1 real-world use — remove duplicates from a list.
lst = [1, 2, 2, 3, 3, 4, 1]
unique = set(lst)
print(unique)          # {1, 2, 3, 4}
print(list(unique))    # back to list (order lost!)

