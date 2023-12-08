import pandas as pd
import calendar 
import random
from tkinter import *
from tkinter import ttk

months = [5, 9, 10, 11]
dfs = []
menu = []
menuHelper = []
for eachM in months:
    sheets = pd.ExcelFile('./'+str(eachM)+"월 월간 메뉴표.xlsx").sheet_names
    for eachS in sheets:
        df = pd.read_excel('./'+str(eachM)+"월 월간 메뉴표.xlsx", sheet_name=eachS, skiprows=[0,1,2,14,15,16])
        # print(df)
        temp = list()
        for eachD in df.columns:
            if eachD not in ['월', '화', '수', '목', '금']:
                temp.append(eachD)
        df = df.drop(columns=temp)
        dfs.append(df)

for eachDF in dfs:
    for eachIndex in eachDF.index[1::2]:
        for eachD in ['월', '화', '수', '목', '금']:
            temp = eachDF.at[eachIndex, eachD]
            if type(temp) == str and temp not in menu: 
                menu.append(eachDF.at[eachIndex, eachD])
    
for index in range(0, len(menu)):
    if menu[index].strip() != 'ㅡ' and menu[index].strip() != '. . .':
        menuHelper.append(menu[index].strip())

menu = menuHelper

for index in range(len(menu)):
    if '\n' in menu[index]:
        result = menu[index].split('\n')[0] + " " + menu[index].split('\n')[1]
        menu[index] = result 


menu.remove('피자')

c = calendar.TextCalendar(calendar.MONDAY)
year = 2023
month = 12
index = 0
week = ["월", "화", "수", "목", "금"]
f_week = dict()
for eachW in week:
    temp = list()
    for each in list(c.itermonthdays(year, month))[index::7]:
        temp.append(each)
    f_week[eachW] = temp
    index = index + 1

num_menu = 0
for each in f_week.values():
    num_menu = num_menu + len(each)
    num_menu = num_menu - each.count(0)

forThisMonth = list()
while(True):
    n = random.randint(0, len(menu)-1)
    if menu[n] not in forThisMonth:
        forThisMonth.append(menu[n])
    if len(forThisMonth) == num_menu:
        break

f_menu = f_week.copy()
i = 0
for each in f_week.keys():
    temp = list()
    for eachE in f_week[each]:
        if eachE == 0:
            temp.append(' ')
        else:
            temp.append(forThisMonth[i])
            i = i + 1
    f_menu[each] = temp

df_menu = pd.DataFrame(data=f_menu)
df_menu.to_excel('./menu' + str(year) + "_" + str(month) + ".xlsx", index=False)

win = Tk()
win_w = 250
win_h = 250
w = win.winfo_screenwidth()//2 - win_w//2
h = win.winfo_screenheight()//2 - win_h//2
win.geometry(str(win_w)+"x"+str(win_h)+"+"+str(w)+"+"+str(h))

def display_text():
   global entry
   info = entry.get()
   label.configure(text=info)
   print(info)

label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

ttk.Button(win, text= "Click",width= 20, command= display_text).pack(pady=20)

win.mainloop()
