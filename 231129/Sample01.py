temp = [11,12,13,14,15,16,17,18,19,101,14,14]

def f1(value:int) -> None:
    index = 0
    for each in temp:
        if each == value:
            print(index)
        index = index + 1


def f2(value:int) -> list:
    result = list()
    index = 0
    for each in temp:
        if each == value:
            result.append(index)
        index = index + 1
    return result

f1(14)
print(f2(14))