import pandas as pd
import os
import calendar 
import random
from datetime import datetime
import tkinter


class Menu:
    dish = list()
    week = ['월', '화', '수', '목', '금']
    calendarList = list()
    menuList = list()

    def makePool(self) -> list: 
        for eachFile in os.listdir('./'):
            if 'xlsx' in eachFile:
                file_name = eachFile
                sheets = pd.ExcelFile(file_name)

                for eachS in sheets.sheet_names:
                    df = pd.read_excel(file_name, sheet_name=eachS, skiprows=[0,1,2,14,15,16])
                    dropList = list()
                    for each in df.columns:
                        if each not in self.week:
                            dropList.append(each)

                    df = df.drop(columns=dropList)

                    for each in df.index[1::2]:
                        for w in self.week:
                            if type(df.at[each, w]) == str:
                                self.dish.append(df.at[each, w])

        return self.dish[:-1]

    def wordFilter(self, target:list):
        '''
        filter each word and put them in a tuple and return it
        '''
        result = list()
        for each in target:
            word = each.strip()
            if '\n' in word:
                for other in word.split('\n'):
                    if other != '\n':
                        result.append(other)
            else:
                if word != 'ㅡ':
                    result.append(word)
        self.dish = tuple(result)


    def addDish(self, name):
        self.dish.append(name)

    def makeCalendar(self, year, month):
        c = calendar.TextCalendar(calendar.MONDAY)
        result = list()
        con = False
        for i in c.itermonthdays(year, month):
            if i == 0 and not con:
                result.append(None)
            elif i == 0 and con :
                pass
            else:
                result.append(i)
                con = True

        self.calendarList = self.listHelper(result)
    
    def listHelper(self, target:list) -> list:
        if target.count(None) >= 5:
            return target[7:]
        else:
            return target
        
    def makeMenuList(self):
        result = []
        cnt = 0
        while(cnt < len(self.calendarList)):
            temp = self.dish[random.randint(0, len(self.calendarList)-1)]
            if temp not in result:
                result.append(temp)
                cnt = cnt + 1

        self.menuList = result

    def makeDict(self) -> dict:
        index = 0
        result = dict()

        print(result)

      
    def run(self):
        self.wordFilter(self.makePool())
        self.makeCalendar(2023, 1)
        self.makeMenuList()
        print(len(self.calendarList))
        print(len(self.menuList))
        # print(self.makeDict())
        # self.menuList = self.chooseDish(self.makeCalendar(2023, 1))
        # self.makeExcel()

if __name__ == "__main__":
    Menu().run()





# class Menu:
#     dish = list()
#     menuList = list()
#     week = ['월', '화', '수', '목', '금']

#     def makePool(self) -> list: 
#         for eachFile in os.listdir('./'):
#             if 'xlsx' in eachFile:
#                 file_name = eachFile
#                 sheets = pd.ExcelFile(file_name)

#                 for eachS in sheets.sheet_names:
#                     df = pd.read_excel(file_name, sheet_name=eachS, skiprows=[0,1,2,14,15,16])
#                     dropList = list()
#                     for each in df.columns:
#                         if each not in self.week:
#                             dropList.append(each)

#                     df = df.drop(columns=dropList)

#                     for each in df.index[1::2]:
#                         for w in self.week:
#                             if type(df.at[each, w]) == str:
#                                 self.dish.append(df.at[each, w])

#         return self.dish[:-1]

#     def wordFilter(self, target:list) -> tuple:
#         '''
#         filter each word and put them in a tuple and return it
#         '''
#         result = list()
#         for each in target:
#             word = each.strip()
#             if '\n' in word:
#                 for other in word.split('\n'):
#                     if other != '\n':
#                         result.append(other)
#             else:
#                 if word != 'ㅡ':
#                     result.append(word)
#         self.dish = tuple(result)

#         return tuple(result)

#     def makeCalendar(self, year, month) -> list:
#         c = calendar.TextCalendar(calendar.MONDAY)
#         result = list()
#         num = False
#         for i in c.itermonthdays(year, month):
#             if i == 0:
#                 if not num:
#                     result.append(None)
#             else:
#                 result.append(i)
#                 num = True

#         return result
    
#     def addDish(self, name):
#         self.dish.append(name)

#     def chooseDish(self, calendar:list) -> list:
#         cnt = 0
#         n = 0
#         result = list()
#         for each in calendar:
#             if each != None:
#                 cnt = cnt + 1
#             else:
#                 n = n + 1
 
#         for each in range(n):
#             result.append(' ')

#         while(len(result)<cnt+n):
#             temp = self.dish[random.randint(0, len(self.dish)-1)]
#             if temp not in result:
#                 result.append(temp)

#         return result

#     def makeDict(self) -> dict:
#         result = dict()
#         index = 0
#         for eachDay in self.week:
#             temp = list()
#             for each in self.menuList[index::5]:
#                 temp.append(each)
#             index = index + 1
#             result[eachDay] = temp

#             print(result)

#         return result
    
#     def makeExcel(self):
#         # datetime object containing current date and time
#         now = datetime.now()
#         df = pd.DataFrame(data=self.makeDict())
#         print(self.makeDict())
#         df.to_excel('./Menu'+str(now.year)+str(now.month)+str(now.day)+'.xlsx',index=False)


#     def run(self):
#         self.wordFilter(self.makePool())
#         self.menuList = self.chooseDish(self.makeCalendar(2023, 1))
#         self.makeExcel()


# if __name__ == "__main__":
#     # Menu().run()
#     m = Menu()
#     print(m.makeCalendar(2023, 1))
#     print(m.makeDict())