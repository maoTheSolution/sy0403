def makeEmptyStack():
    '''
    return an empty list
    '''
    return list()

def pushElement(e, s:list):
    '''
    push an element into the stack
    '''
    s.insert(0, e)

def takeOut(s:list):
    '''
    take out the first one in the stack and remove it 
    '''
    temp = s[0]
    s.remove(temp)
    return temp

def display(s:list):
    for each in range(len(s)):
        print(each, " : ",  s[each])

def getStackSize(target):
    return len(target)

if __name__ == '__main__':
    target = makeEmptyStack()
    display(target)
    pushElement('Apple', target)
    # display(target)
    pushElement('Banana', target)
    pushElement('Pear', target)
    pushElement('Melon', target)
    # display(target)
    takeOut(target)
    display(target)
    print("The size of the stack is ",  getStackSize(target))

