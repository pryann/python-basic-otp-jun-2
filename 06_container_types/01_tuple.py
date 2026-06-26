# indexed
# ordered
# immutable
# allow duplicates
# can contains any type of data

rgb = (255, 34, 55)

print(rgb, type(rgb))
print(rgb.count(34))
print(rgb.index(34))

coordinates = (34.55343, 123.111)


def stat(numbers):
    return min(numbers), max(numbers)


result = stat([1, 2, 3, 4, 5, 6, 7])
print(result, type(result))

# fmt: off
one_element = (1)
print(type(one_element))
# fmt: on
one_element = (1,)
print(type(one_element))
