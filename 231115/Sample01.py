def readFile(location) -> list:
    f = open(location, 'r')
    words = f.read().split(' ')

    return words