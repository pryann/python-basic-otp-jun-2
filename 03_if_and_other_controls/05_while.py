for i in range(0, 6, 1):
    print(i)

i = 0
while i < 6:
    print(i)
    i += 1


while True:
    grade = input("Adj meg egy osztályzatot (1-5)")
    if grade.isdigit() and 0 < int(grade) < 6:
        print("Ez egy érdemjegy")
        break
    print("Ez NEM érdemjegy")
