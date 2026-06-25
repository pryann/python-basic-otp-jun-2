yearly_salaries = [60_000, 70_000, 80_000, 90_000]

yearly_salaries_copy = yearly_salaries

print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))

yearly_salaries.append(200_000)
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))

# -----------------------------------------
# [60_000, 70_000, 80_000, 90_000]            <--- yearly_salaries
#                                             <--- yearly_salaries_copy
# -----------------------------------------

# -----------------------------------------
# [60_000, 70_000, 80_000, 90_000, 200_000]   <--- yearly_salaries
#                                             <--- yearly_salaries_copy
# -----------------------------------------

yearly_salaries_copy.pop()
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))

yearly_salaries = [1, 2, 3]
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))
# -----------------------------------------
# [60_000, 70_000, 80_000, 90_000]
#                                             <--- yearly_salaries_copy
# -----------------------------------------
# [1, 2 ,3 ]                                 <--- yearly_salaries
# -----------------------------------------
