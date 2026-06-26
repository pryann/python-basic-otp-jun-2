# key value pairs
# mutable type as key
# value can be any type of data
# unique keys

user = {
    "name": "John Doe",
    "age": 33,
}

print(user["name"])

user["age"] = 18
print(user)

user["job"] = "teacher"
print(user)

user["hobbies"] = ["reading", "music listening"]
print(user)

user.pop("hobbies")
print(user)

user.update({"age": 50, "salary": 120_000})
print(user)

print(user.keys())
print(user.values())
print(user.items())

for i in user:
    print(i)


for i in user.values():
    print(i)


for k, v in user.items():
    print(k, v)
