class Student:
    __name = None
    __id = None

    def __init__(self, name, id) -> None:
        self.__name = name
        self.__id = id

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def display(self):
        print(self.__name, self.__id)




s1 = Student("Adam", "123AAC")

def makeStudent(name, id) -> Student:
    return Student(name, id)

makeStudent("SY", "1234AACCC").display()
