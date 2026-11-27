# Find duplicate values in a list in Python
from collections import Counter

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 3]

# 1. Using Counter
counts = Counter(numbers)
duplicates = [num for num, c in counts.items() if c > 1]
print("Duplicates (Counter):", duplicates)

# 2. Using a set
seen, dupes = set(), set()
for n in numbers:
    if n in seen:
        dupes.add(n)
    else:
        seen.add(n)
print("Duplicates (set)    :", sorted(dupes))

# 3. Remove duplicates, keep order
unique = list(dict.fromkeys(numbers))
print("Unique values       :", unique)

# 4. Count of each duplicate
print("Duplicate counts    :", {k: v for k, v in counts.items() if v > 1})
