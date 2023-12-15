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
        self.makeUsers(10)
        print(self.users)
        

if __name__ == "__main__":
    m = MBTI()
    m.ready()
    


    
        
    
    
        

    