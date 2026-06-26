def calculate_gross_price(net_price, vat_percent=27):
    return net_price * (1 + vat_percent / 100)


print(calculate_gross_price(1000))
print(calculate_gross_price(2000))
print(calculate_gross_price(10_000))
print(calculate_gross_price(100_000, 5))
# print(calculate_gross_price(net_price=100_000, vat_percent=5))


# def add_to_basket(item, basket=[]):
#     basket.append(item)
#     return basket


def add_to_basket(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


basket = []
print(add_to_basket("apple"))
print(add_to_basket("banana"))
print(add_to_basket("orange"))
