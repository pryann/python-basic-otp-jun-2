import random
from datetime import datetime, date, time

num = random.randint(1, 100)
print(num)

numbers = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(numbers)
print(numbers)

print(random.choice(numbers))

print(datetime.now())
print(datetime(2020, 10, 1))
# https://docs.python.org/3/library/datetime.html
print(datetime(2020, 10, 1).strftime("%Y %B %d."))
print(datetime(2020, 10, 1).isoformat())
print(datetime(2020, 10, 1) - datetime(2020, 9, 4))

d = date(2020, 1, 1)
print(d)
t = time(12, 12, 12, 123456)
print(t)
print(datetime.combine(d, t))
