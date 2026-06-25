# int_value = int("10") # 10
# int_value = int(True) # 1
# int_value = int(False)  # 0
# int_value = int("10a")  # ValueError
int_value = int("-10")
print(int_value, type(int_value))

float_value = float("10.10")
print(float_value)  # 10.1

float_value = float(11)
print(float_value)  # 11.0

float_value = float("10e10")
print(float_value)  # 100000000000.0
