def elem(data):
    elem = list(set(data))
    return elem

test = [1, 2, 4, 5, 6, 7, 8, 9, 10, 10]

result = elem(test)
print(result)