
# you can write a file and save it
# f = open('./temp.txt', 'w')
# f.write('hello')

def readFile(location) -> list:
    f = open(location, 'r')
    return f.read().split(' ')


def makeDict(sampleList) -> dict:
    result = dict()
    for each in sampleList:
        if each in result:
            result[each] = result[each] + 1
        else:
            result[each] = 1

    return result

def returnTheMax(sampleDict)->str:
    for each in sampleDict.keys:
        # sampleDict[each] ==> value



if __name__ == "__main__":
    temp = readFile('./given.txt')
    print(makeDict(temp))
