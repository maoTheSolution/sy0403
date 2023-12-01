# pip install xlrd openpyxl pandas

import pandas as pd

file_name = './10월 월간 메뉴표.xlsx'
df = pd.read_excel(file_name)
print(df)