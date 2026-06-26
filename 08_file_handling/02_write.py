with open("new.txt", "w", encoding="UTF-8") as f:
    f.write("Ollé")


lines = ["first\n", "second\n", "third"]
with open("new2.txt", "w", encoding="UTF-8") as f:
    f.writelines(lines)

