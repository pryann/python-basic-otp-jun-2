print(True, type(True))
print(False, type(False))

yearly_salary = 100_000
high_salary_treshold = 180_000

# ==, !=, >, <, <=, >=, is, is not, in, not in
if yearly_salary > high_salary_treshold:
    print("High salary")
else:
    print("Low salary")

grade = input("Adj meg egy érdemjegyet! (1-5)")

if grade == "1":
    print("Elégtelen")
elif grade == "2":
    print("Elégséges")
elif grade == "3":
    print("Közepes")
elif grade == "4":
    print("Jó")
elif grade == "5":
    print("Jeles")
else:
    print("Ez nem osztályzat")
