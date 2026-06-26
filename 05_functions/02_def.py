def greeting(name):
    print(f"Hi {name}")


greeting("John")
greeting("Jane")
print(greeting("Jane"))


def greetings(name):
    return f"Hi {name}"


result = greetings("John")
print(result)
print(greetings("Jane"))
