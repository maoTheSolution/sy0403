import pandas as pd
import calendar 

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
            if type(temp) == str: 
                menu.append(eachDF.at[eachIndex, eachD])
    

for index in range(0, len(menu)):
    if menu[index].strip() != 'ㅡ' and menu[index].strip() != '. . .':
        menuHelper.append(menu[index].strip())

menu = menuHelper

for index in range(len(menu)):
    if '\n' in menu[index]:
        result = menu[index].split('\n')[0] + " " + menu[index].split('\n')[1]
        menu[index] = result 


print(menu)

# c = calendar.TextCalendar(calendar.MONDAY)
# print(c)

# for i in c.itermonthdays(2023, 12):
#     if i ==0:
#         result.append(None)
#     else :
#         result.apppend(i)

# print(result)
