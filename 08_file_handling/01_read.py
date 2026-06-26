with open("text.txt", "r", encoding="UTF-8") as f:
    print(f.read())
    f.seek(0)
    print(f.read())
    f.seek(0)
    print(f.readline())
    print(f.readline())
    print(f.readline())
    f.seek(0)
    print(f.readlines())
    f.seek(0)

    for i in f:
        print(i, end="")

    f.seek(0)

    content = f.read()
    print(content)
