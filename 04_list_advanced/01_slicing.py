yearly_salaries = [60_000, 70_000, 80_000, 90_000, 100_000, 110_000, 120_000]

print("to the 2.:", yearly_salaries[:2])
print("from the 2.:", yearly_salaries[2:])
print("from the 2. to the 5.:", yearly_salaries[2:5])
print("from the 0. to the 6. step 2:", yearly_salaries[:6:2])
print("odd", yearly_salaries[::2])
print("last", yearly_salaries[-1])
print("last", yearly_salaries[::-1])

# yearly_salaries_copy = yearly_salaries.copy()
yearly_salaries_copy = yearly_salaries[:]

yearly_salaries[0:2] = [65_000, 75_000]
print(yearly_salaries)
