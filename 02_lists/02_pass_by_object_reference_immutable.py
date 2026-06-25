age = 33
age_copy = age

print(age, id(age))
print(age_copy, id(age_copy))

# -----
# 33      <---- age
#         <---- age_copy = age
# -----

age = 18
print(age, id(age))
print(age_copy, id(age_copy))


# -----
#  33       <---- age_copy
# -----
#  18       <---- age
# -----
