def recursive_gcd(a, b):
    # if b == 0:
    #     return a
    # else:
    #     return recursive_gcd(b, a % b)

    return a if b == 0 else recursive_gcd(b, a % b)


print(recursive_gcd(11, 33))
