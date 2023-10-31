import random as r


def makeList() -> list:
    '''
    return a list which consists of 101 different elements 
    '''
    saved = list()
    while(True):
        temp = r.randint(0, 101)
        if temp not in saved:
            saved.append(temp)
        if len(saved) == 101:
            break

    return saved


def display(sampleList:list) -> None:
    '''
    print out all the elements in the given list
    '''
    for each in sampleList:
        print(each, end=" ")
    print()


def randomIntGen(sampleList:list) -> int:
    return r.randint(0, len(sampleList)-1)

def lotto(sampleList:list) -> list:
    l = list()
    while(True):
        temp = randomIntGen(sampleList)
        if temp not in l:
            l.append(temp)
        if len(l) == 6:
            break

    return l
    

if __name__ == '__main__':
    temp01 = makeList()
    display(temp01)
    display(lotto(temp01))