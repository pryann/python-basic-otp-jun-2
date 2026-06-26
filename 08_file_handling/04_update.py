with open("new2.txt", "r+", encoding="UTF-8") as f:
    content = f.readlines()
    content = [i.capitalize() for i in content]
    content.append("\nforth")
    f.seek(0)
    f.writelines(content)
