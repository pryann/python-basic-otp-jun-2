# ordered
# indexed
# mutable
# allow duplicated member
# can contains any type of data
yearly_salaries = [80_000, 90_000, 100_000, 110_000, 60_000]
print(yearly_salaries, type(yearly_salaries))

print(yearly_salaries[0])
print(len(yearly_salaries))

print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)

yearly_salaries[0] = 0
print(yearly_salaries)

# delete by index
del yearly_salaries[0]
print(yearly_salaries)

yearly_salaries.append(200_000)
print(yearly_salaries)

yearly_salaries.extend([1, 2, 3])
print(yearly_salaries)

yearly_salaries.insert(1, 1000)
print(yearly_salaries)

# ValueError if not exists
yearly_salaries.remove(1000)
print(yearly_salaries)

# delete by index, default, the last item
yearly_salaries.pop()
print(yearly_salaries)

yearly_salaries.extend([1, 1, 1])
print(yearly_salaries.count(1))

yearly_salaries.sort(reverse=True)
print(yearly_salaries)

yearly_salaries.reverse()
print(yearly_salaries)

user = ["My", "name", "is", "John", "Doe"]
user_sentence = " ".join(user)
print(user_sentence)
print(user_sentence.split(" "))
