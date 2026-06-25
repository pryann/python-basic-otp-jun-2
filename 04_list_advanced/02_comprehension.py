net_prices = [1000, 2000, 10000]
vat_percent = 27
# gross_prices = []

# for price in net_prices:
#     gross_prices.append(price * (1 + vat_percent / 100))

# print(gross_prices)

gross_prices = [i * (1 + vat_percent / 100) for i in net_prices]
print(gross_prices)

values = [1, 2, 3, 4, 5, 6, 6, 4, 3, 2, 7, 8, 9]
grades = [i for i in values if 0 < i < 6]

# for i in values:
#     if 0 < i < 6:
#         grades.append(i)


matrix = [[j for j in range(5)] for _ in range(5)]
print(matrix)
