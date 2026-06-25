name = "John Doe"

print(len(name))
print(name[0])
print(name[7])
# IndexError
# print(name[10])
# TypeError: 'str' object does not support item assignment
# IMMUTABLE
# name[0] = "j"

# name = "john doe"
print(name.lower())
print(name.capitalize())
print(name.find("o"))
print(name.count("o"))
print(name.replace("o", "oo"))
print("   Gergely  ".strip())
