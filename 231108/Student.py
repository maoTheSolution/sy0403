class Student:
    name = None
    age = None
    sex = None

    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex
    # setter
    def setName(self, name):
        self.name = name
    
    def setAge(self, age):
        self.age = age
    
    def setSex(self, sex):
        self.sex = sex

    # getter
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getSex(self):
        return self.sex
    
    def display(self):
        print(self.name, self.age, self.sex)






