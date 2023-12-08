import calendar

c = calendar.TextCalendar(calendar.MONDAY)
year = 2023
month = 2
index = 0
week = ["월", "화", "수", "목", "금"]
f_week = dict()
for eachW in week:
    temp = list()
    for each in list(c.itermonthdays(year, month))[index::7]:
        temp.append(each)
    f_week[eachW] = temp
    index = index + 1

    