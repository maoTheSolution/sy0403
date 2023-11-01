import random

def f1() -> list:
    temp = list() # temp = []
    while(True):
        num = random.randint(1, 100)
        if num not in temp:
            temp.append(num)
        if len(temp) == 100:
            break

    return temp


def display(sampleList: list) -> None:
    cnt = 0
    for each in sampleList:
        cnt = cnt + 1
        print(each, end="\t")
        if cnt % 10 == 0:
            print()

def f2(sList:list) -> int:
    return sList[random.randint(0, len(sList)-1)]


def f3():
    t1 = f1()
    result = list()
    cnt = 0
    while(True):
        value = f2(t1)
        if value not in result:
            result.append(value)
            cnt = cnt + 1
        if cnt == 6:
            break
    
    return result


if __name__ == '__main__':
    display(f3())