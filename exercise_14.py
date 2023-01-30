def combined(dict1, dict2):
    com = {}

    for key in dict1.keys():
        if key in dict2.keys():
            com[key] = dict1[key] + dict2[key]
    return com

dict1 = {'a': 5, 'b': 12, 'c': 3, 'd' :9}
dict2 = {'b': 4, 'c': 9, 'd': 10, 'e' :19}
combina = combined(dict1, dict2)
print(combina)