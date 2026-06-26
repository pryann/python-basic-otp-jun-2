net_price = 1000
vat_percent = 27
gross_price = None


# DO NOT DO THIS!!!!
# no params
# not pure
# not reusable
def calculate_gross_price():
    # print(gross_price)
    global gross_price
    gross_price = net_price * (1 + vat_percent / 100)
    print(gross_price)


calculate_gross_price()
print(gross_price)
