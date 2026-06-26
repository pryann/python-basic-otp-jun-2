def double(numbers):
    return [i * 2 for i in numbers]


print(double([1, 2, 3, 4]))  # [2, 4, 6, 8]


# 2. Palindrom-e a string (slicing)
def palindrom(text):
    return text == text[::-1]


print(palindrom("görög"))  # True
print(palindrom("alma"))  # False


# 3. Két lista közös elemei (comprehension)
def list_union(list1, list2):
    return [elem for elem in list1 if elem in list2]


print(list_union([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]


# 4. n-edik Fibonacci-szám (rekurzió)
def fibonacci(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))  # 55
print(fibonacci(-3))  # None


# 5. Prímszám-e (bool)
def prim(number):
    if number < 2:
        return False
    for div in range(2, int(number**0.5) + 1):
        if number % div == 0:
            return False
    return True


print(prim(7))  # True
print(prim(10))  # False
