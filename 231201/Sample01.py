# pip install xlrd openpyxl pandas

import pandas as pd
import math

file_name = './10월 월간 메뉴표.xlsx'
sheets = pd.ExcelFile(file_name)

dish = list()

for each in sheets.sheet_names:
    df = pd.read_excel(file_name, sheet_name=each, skiprows=[0,1,2,14,15,16])
    dropList = []
    week = ['월', '화', '수', '목', '금']
    for each in df.columns:
        if each not in week:
            dropList.append(each)

    df = df.drop(columns=dropList)


    for each in df.index[1::2]:
        for w in week:
            if type(df.at[each, w]) == str:
                dish.append(df.at[each, w])

for each in dish:
    print(each)



