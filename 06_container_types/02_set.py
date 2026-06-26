# unordered
# unindexed
# contains uniqe values

from enum import unique


numbers = {1, 2, 3}
print(numbers, type(numbers))

# TypeError: 'set' object is not subscriptable
# numbers[0]

numbers.add(4)
print(numbers)

numbers.update([5, 6, 7])
print(numbers)

# KeyError: 10
# numbers.remove(10)
# print(numbers)

# do not raise error if not found
numbers.discard(10)

numbers.pop()
print(numbers)

x1 = {"a", "b", "c"}
x2 = {"b", "c", "d"}

print(x1.union(x2))
print(x1.intersection(x2))
print(x1.difference(x2))
print(x1.symmetric_difference(x2))
print({"b"}.isdisjoint(x2))
print(x1.issubset({"a", "b", "c", "d"}))
print(x1.issuperset({"a", "b"}))

values = [1, 2, 3, 4, 5, 6, 7, 3, 5, 2, 2, 3, 5, 3, 2, 4, 5]
unique_values = list(set(values))
print(unique_values)
