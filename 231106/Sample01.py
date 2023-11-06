class Student:
    name = None
    age = None
    id = None
    sex = None

    def __init__(self, name, age, id, sex) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.sex = sex

    # getter
    def getName(self): 
        return self.name

    def getAge(self):
        return self.age
    
    def getId(self):
        return self.id

    def getSex(self):
        return self.sex
    
    # setter
    def setName(self, newName):
        self.name = newName

    def setAge(self, newAge):
        self.age = newAge

    def setId(self, id):
        self.id = id

    def setSex(self, sex):
        self.sex = sex

    def display(self):
        print(self.name)
        print(self.age)
        print(self.id)
        print(self.sex)

    


s1 = Student("SY", 18, "123456789A", 'F')
s2 = Student("YG", 20, "123456678B", 'M')
s1.display()
s2.display()


