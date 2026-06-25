# 5. Írj egy Python programot, amely kiírja egy szöveg minden második karakterét!
text = "Hello Py"
for i in range(0, len(text), 2):
    print(text[i])

# 6. Adott egy lista, amely számokat tartalmaz.
# Írj egy programot, amely meghatározza a lista elemeinek összegét a következő feltételek szerint:
# ha az elem pozitív, akkor az összegbe kerüljön be, ha negatív, akkor ne!
numbers = [-1, -2, -3, 0, 1, 2, 3]
total = 0

for i in numbers:
    if i > 0:
        total += i

print(total)


# 7.  Írj egy Python programot, amely kiírja a listában található összes számot,
# ami 3-mal vagy 4-gyel vagy 5-tel osztható!

numbers = [3, 4, 12, 10, 6, 7]
dividers = [3, 4, 5]
good = []

for number in numbers:
    for divider in dividers:
        if number % divider == 0 and number not in good:
            good.append(number)

print(good)
