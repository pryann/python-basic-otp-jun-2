# 1. Írj egy Python függvényt, amely kap két egész számból álló tuple-t, és visszaadja az összegüket és szorzatukat is egy tuple-ben!
# (1,2,3) (4,5,6)
# 1+2+3+4+5+6
# 1*2*3*4*5*6


def tuple_stat(tuple1, tuple2):
    concated_tuple = tuple1 + tuple2
    multi = 1 if len(concated_tuple) > 0 else 0
    for i in concated_tuple:
        multi *= i
    return sum(concated_tuple), multi


print(tuple_stat((1, 2, 3), (4, 5, 6)))


# 2. Írj egy függvényt,paraméterként kap egy szótárat és egy listát, a lista stringeket tartalmaz,  a függvény a szótárból eltávolítja azokat a kulcs-érték párokat, amelyek kulcsa nem szerepel a kulcsokat tartalmazó listában!
# {"a": "a", "b": "b", "c": "c"}
# ["a", "b"]
# {"a": "a", "b": "b"}
def filter_dict(data: dict, keys_list):
    for key in list(data):
        if key not in keys_list:
            data.pop(key)
    return data


print(filter_dict({"a": "a", "b": "b", "c": "c"}, ["a", "b"]))


# 3.  Írj egy Python függvényt, amely egy adott listában megkeresi az összes ismétlődő elemet, majd létrehoz és visszaad egy set-et, amely tartalmazza az ismétlődő  elemeket. Például az [1, 2, 3, 2, 4, 3] lista esetén a vissza adott set tartalmazza az 2 és 3 elemeket!
def get_duplicates(custom_list):
    unique = set()
    duplicated = set()
    for i in custom_list:
        if i in unique:
            duplicated.add(i)
        else:
            unique.add(i)
    return duplicated


print(get_duplicates([1, 2, 3, 4, 5, 3, 4, 5]))
