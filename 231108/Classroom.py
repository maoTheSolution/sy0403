import Student as s

class Classroom:
    studentList = list()

    def __init__(self, num) -> None:
        for each in range(num):
            name = input("Enter you name : ")
            age = input("Enter your age : ")
            sex = input("Enter your sex : ")
            self.studentList.append(s.Student(name, age, sex))
        
