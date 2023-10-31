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




if __name__ == '__main__':
    temp01 = makeList()
    temp02 = makeList()
    display(temp01)
    display(temp02)