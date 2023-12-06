import pandas as pd
months = [5, 9, 10, 11]
dfs = []
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
    for eachIndex in eachDF.index:
        for eachD in ['월', '화', '수', '목', '금']:
            print(eachDF.at[3, eachD])
        
            











# import calendar 

# def makeCalendar(year, month) -> list:
#     c = calendar.TextCalendar(calendar.MONDAY)
#     result = list()

#     for i in c.itermonthdays(year, month):
#         if i == 0:
#             result.append(None)
#         else:
#             result.append(i)

#     return result

# print(makeCalendar(2023, 12))





