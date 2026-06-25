yearly_salaries = [80_000, 90_000, 100_000, 110_000, 60_000]
high_salary_treshold = 100_000
total_low_salaries = 0
total_high_salaries = 0

for yearly_salary in yearly_salaries:
    if yearly_salary > high_salary_treshold:
        total_high_salaries += yearly_salary
    else:
        total_low_salaries += yearly_salary

print(total_low_salaries)
print(total_high_salaries)
