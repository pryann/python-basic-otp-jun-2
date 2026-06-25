print("banana")
# fmt: off
print('banana')
print('I\'m a teacher')
print("I'm a teacher")
# fmt: on
print("First line\nsecond line\nthird line")
print("""First line 
second line
third line""")

# triple ': docstring

first_name = "Gergely"
last_name = "Gáll"
age = 42
full_name = first_name + last_name
print(first_name * 3)
print(full_name)

# me = "My name is " + first_name + " " + last_name + " and I'm " + str(age) + " years old."
# me = "My name is {0} {1} and I'm {2} years old.".format(first_name, last_name, age)
me = f"My name is {first_name} {last_name} and I'm {age} years old."
print(me)

print(10 + 10)
print(10 + 10.10)
print("10" + "10")
# TypeError
# print(10 + "10")
