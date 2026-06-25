first_name = "John"
last_name = "Doe"
age = 33

first_name, last_name, age = "Jane", "Doo", 18

# data swap
a = 10
b = 20

# tmp = a
# a = b
# b = tmp

a, b = b, a
print(a, b)

# unpacking
abc = "abc"
a, b, c = abc
print(a, b, c)

user = ["John", "Doe", 33]
first_name, last_name, age = user
print(first_name, last_name, age)

user = ["John", "Doe", 33, "techer", ["reading", "music listening"]]
first_name, last_name, age, *_ = user
print(first_name, last_name, age)

numbers = [1, 2, 3, 4, 5, 6]
first, second, *_, last = numbers
print(first, second, last)
