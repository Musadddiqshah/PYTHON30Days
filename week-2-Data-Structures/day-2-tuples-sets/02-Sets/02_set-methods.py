# ===== set() methods =====

# 1. add() method — add ONE item.
nums = {1, 20, 2, 29, 6}
nums.add(8)
nums.add(1)  # adding duplicate does nothing (sets remove duplicates automatically)
print(nums)

# 2. update() — add MANY items.
nums = {4, 5, 6, 7}
nums.update([1, 2, 3])
print(nums)

names = {'Musaddiq'}
names.update(['Yaseen', 'Mutee', 'Faheem'])
print(names)
print(len(names)) # 4

# 3. remove() — remove an item. Reteurn KeyError if not found.
nums = {1, 7, 9, 5, 8}
nums.remove(5)
# nums.remove(77)  # KeyError — 77 is not in the set
print(nums)

# 4. discard() — SAFER than remove(). No error if item not found.
nums = {18, 28, 26, 12}
nums.discard(26)
nums.discard(29)  # no error — discard is safe
print(nums)

# 5. pop() — removes an ARBITRARY item (not random, just arbitrary) and returns it.
nums = {1975, 1990, 2000, 2008}
nums.pop()
print(nums)  #  not "random" — not chosen randomly, just whatever
             # is first in the set's internal order. Don't rely on which one is removed.

# 6. clear() — delete everything in set.
nums = {17, 8, 96, 4, 7}
nums.clear()
print(nums)  # prints set() — empty set

# 7. Loop over sets — same as list, so we will skip.

# 8. Set maths — union ( | ) / .union() — all items from both, no duplicates.
num1 = {12, 13, 14, 16}
num2 = {77, 27, 1, 9, 10}
print(num1 | num2)          # both are same
print(num1.union(num2))     # returns a NEW set with items from both

# 9. intersection ( & ) / .intersection() — items in BOTH sets.
a = {1, 7, 77, 69, 20}
b = {82, 28, 1, 20, 77}
print(a.intersection(b))    # {1, 20, 77}
print(a & b)                # same

# 10. difference ( - ) / .difference() — items in `a` but NOT in `b`.
# IMPORTANT: a - b is NOT equal to b - a (direction matters).
print(a - b)                # {7, 69}
print(a.difference(b))      # same

# symmetric_difference ( ^ ) / .symmetric_difference() — items in ONE, not both.
print(a ^ b)                          # {7, 69, 82, 28}
print(a.symmetric_difference(b))      # same

# subset / superset / disjoint checks.
small = {1, 2, 3}
big   = {1, 2, 3, 4, 5}
print(small.issubset(big))    # True  — all of small is in big
print(big.issuperset(small))  # True  — big contains all of small
print({1, 2}.isdisjoint({3, 4}))   # True — no common items

#  copy() — real copy (fixes the `b = a` trap).
x = {1, 2, 3}
y = x.copy()      # safe copy
y.add(4)
print(x)          # {1, 2, 3} — unchanged
print(y)          # {1, 2, 3, 4}

# ⚠️ The TRAP without copy():
p = {1, 2, 3}
q = p             # q and p point to the SAME set
q.add(4)
print(p)          # {1, 2, 3, 4} — p also changed!

# End of sets. Not complete — check python.org for more (issubset, frozenset, etc.)
# Written by Musaddiq Shah on 31,10,2026.
