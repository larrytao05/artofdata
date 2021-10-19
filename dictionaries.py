def count(strings) :
    Dict = {}
    for string in strings:
        if string in Dict.keys():
            Dict[string] += 1
        else:
            Dict[string] = 1
    return Dict



strings = ["dadad", "2ad21e3","dadad"]
Dict2 = count(strings)
print(Dict2)
for (k, v) in Dict2.items():
    print(k)
    print(v)
