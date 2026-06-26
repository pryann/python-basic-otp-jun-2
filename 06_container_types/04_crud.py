users = [
    {"id": 1, "first_name": "Marina", "last_name": "Cordle", "email": "mcordle0@narod.ru"},
    {"id": 2, "first_name": "Ric", "last_name": "Ullyott", "email": "rullyott1@51.la"},
    {"id": 3, "first_name": "Gaye", "last_name": "Bindon", "email": "gbindon2@topsy.com"},
    {"id": 4, "first_name": "Emlynn", "last_name": "Ticehurst", "email": "eticehurst3@creativecommons.org"},
    {"id": 5, "first_name": "Raleigh", "last_name": "Durrant", "email": "rdurrant4@livejournal.com"},
    {"id": 6, "first_name": "Rubia", "last_name": "Liver", "email": "rliver5@scribd.com"},
    {"id": 7, "first_name": "Talbot", "last_name": "Hairon", "email": "thairon6@nifty.com"},
    {"id": 8, "first_name": "Francesco", "last_name": "Carnegy", "email": "fcarnegy7@list-manage.com"},
    {"id": 9, "first_name": "Hayden", "last_name": "Tierny", "email": "htierny8@networkadvertising.org"},
    {"id": 10, "first_name": "Kacie", "last_name": "O'Carroll", "email": "kocarroll9@topsy.com"},
]


def generate_new_id():
    # it works only if the users list is ordered by id
    # return users[-1] + 1
    return max(user["id"] for user in users) + 1


def find_user(id):
    for user in users:
        if user["id"] == id:
            return user
    # return None


print(find_user(10))


def create_user(user_payload):
    # V1: not the best
    # user_payload.update({"id": generate_new_id()})
    # V2: better
    # new_user = {"id": generate_new_id()}
    # new_user.update(user_payload)
    # users.append(new_user)
    # V3: simple
    users.append({"id": generate_new_id(), **user_payload})
    return users[-1]


print(create_user({"first_name": "Jane", "last_name": "Doe", "age": 20}))


def update_user(id, user_payload):
    user = find_user(id)
    if user is not None:
        user.update(user_payload)
        return user


print(update_user(10, {"first_name": "Gergely"}))
print(users)


def remove_user(id):
    user = find_user(id)
    if user is not None:
        users.remove(user)


remove_user(110)
print(users)
