import requests
from bs4 import BeautifulSoup as bs
import random

class MBTI:
    def __init__(self) -> None:
        self.mbti = list()
        self.result = dict()
        self.users = dict()

    def mbtiScore(self):
        url = 'https://testmoa.com/mbti-compatibility/'
        page = requests.get(url)
        soup = bs(page.text, "html.parser")
        for each in soup.find_all('h3',{'class':'wp-block-heading'}):
            self.mbti.append(each.text[:4])
    
        # remove MBTI from the mbti list
        self.mbti = self.mbti[:-1]

        for each in soup.find_all('figure', {'wp-block-table aligncenter is-style-stripes'}):
            for matched in [e.text for e in each.find_all('td')[3] if e.text != ', ' and e.text != ',\xa0']:
                self.result[(each.text[:4], matched.strip())] = 5
            # 좋은 궁합
           
            for matched in [e.text for e in each.find_all('td')[5] if e.text != ', ' and e.text != ',\xa0']:
                self.result[(each.text[:4], matched.strip())]  = 4
            # 최악의 궁합
            for matched in [e.text for e in each.find_all('td')[7] if e.text != ', ' and e.text != ',\xa0']:
                self.result[(each.text[:4], matched.strip())]  = 1


    def makeUsers(self, num):
        while(len(self.users) < num):
            tempName = self.makeName()
            if tempName not in self.users:
                self.users[tempName] = self.chooseMBTI()

    def makeName(self) -> str:
        al = [chr(each) for each in range(97, 123)]
        name = ""
        for each in range(5):
            name = name + al[random.randint(0, 25)]

        return name
    

    def chooseMBTI(self) -> str:
        temp = random.randint(0, len(self.mbti)-1)
        return self.mbti[temp]
    
    def ready(self):
        self.mbtiScore()

    def makeTeam(self, num) -> list:
        temp = list()
        targetList = list(self.users.keys())
        for each in targetList[1:]:
            for other in targetList[:-1]:
                temp.append((self.users[each], self.users[other]))


        for each in temp:
            if each not in self.result:
                self.result[each] = 2
                print(2)
            else:
                print(self.result[each])
        return temp
    

class Person:

    name = None
    mbti = None
    con = None

    def __init__(self, name, mbti, con=True):
        self.name = name
        self.mbti = mbti
        self.con = con

    # getter 
    def getName(self):
        return self.name

    def getMbti(self):
        return self.mbti
    
    def getCon(self):
        return self.con
    
    # setter
    def setName(self, name:str):
        self.name = name
        print("A new name is updated!")

    def setMbti(self, mbti:str):
        self.mbti = mbti
        print("A new mbti is updated!")

    def setCon(self, con:bool):
        self.con = con
        print("A new condition is updated!")

    def display(self):
        print(self.name, " : ", self.mbti, " : ", self.con)


class Matching:
    result = None
    num = None

    def __init__(self) -> None:
        result = list()
        # self.num = num

    # def makeTeam(num):

    def makeTeam(self, target:list, mbti:dict):
        for each in target:
            print(each.getName(), each.getMbti())
        print("*"*100)
        for first in range(0, len(target)-1):
            for second in range(first+1, len(target)):
                print(target[first].getName(), target[first].getMbti(), end=", ")
                print(target[second].getName(), target[second].getMbti())
                try:
                    print(mbti[(target[first].getMbti(), target[second].getMbti())])
                except KeyError:
                    print("2")


    
    

if __name__ == "__main__":
    m = MBTI()
    m.ready()
    personList = list()
    for each in range(10):
        personList.append(Person(m.makeName(), m.chooseMBTI()))
    
    # for each in personList:
    #     each.display()

    helper = Matching()
    helper.makeTeam(personList, m.result)
    



    
        
    
    
        

    