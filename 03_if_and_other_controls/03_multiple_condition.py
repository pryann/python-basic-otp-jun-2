age = 30

if age < 18:
    print("Kiskorú")
# elif age >= 18 and age < 65:
elif 18 <= age < 65:
    print("Felnőtt")
else:
    print("Nyugdíjas")

prog_lang = "Java"

# if prog_lang == "Java" or prog_lang == "Python":
#     print("backend")

backend_languages = ["Java", "Python"]

if prog_lang in backend_languages:
    print("backend")


temperature = 50
humidity = 60
rain = True

# not rain            False
# humidity < 70       True
#                     False and True  =  False
# temperature > 30    True
#                     False or True   =   True
if temperature > 30 or humidity < 70 and not rain:
    print("Dry")

# temperature > 30    True
# humidity < 70       True
#                     True or True     =  True
# not rain            False
#                     True and False   =  False
if (temperature > 30 or humidity < 70) and not rain:
    print("Dry")
