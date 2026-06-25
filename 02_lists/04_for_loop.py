# for ciklusváltozó in sorozat:
#     ciklusmag

for yearly_salary in range(10):
    print(yearly_salary)

for yearly_salary in range(5, 10):
    print(yearly_salary)


for yearly_salary in range(5, 50, 10):
    print(yearly_salary)

for yearly_salary in range(10, 0, -2):
    print(yearly_salary)


yearly_salaries = [60_000, 70_000, 80_000, 90_000]

for yearly_salary in yearly_salaries:
    print(yearly_salary)

for i in range(len(yearly_salaries)):
    print(f"index: {i}, value: {yearly_salaries[i]}")

for index, value in enumerate(yearly_salaries):
    print(f"index: {index}, value: {value}")
