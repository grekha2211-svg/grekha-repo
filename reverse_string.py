# Different ways to reverse a string in Python
text = "Hello, World!"

# 1. Slicing
print("Slicing   :", text[::-1])

# 2. reversed() + join
print("reversed():", "".join(reversed(text)))

# 3. Loop
result = ""
for ch in text:
    result = ch + result
print("Loop      :", result)

# 4. Function
def reverse_string(s):
    return s[::-1]

print("Function  :", reverse_string("Python"))
