import requests as req
from bs4 import BeautifulSoup as bs


url = 'https://www.puppydog.co.kr'
op = '/category/고양이간식/116/'
res = req.get(url+op,  headers={"User-Agent": "Safari 17.1"})
soup = bs(res.text, "html.parser")
# soup.prettify()
# for each in soup.find_all('div', {'class':'sp__product_title_247'}):
#     print(each.text)


titles = soup.find_all('div', {'class':'sp__product_title_247'})
f_titles = list()
for each in titles:
    f_titles.append(each.text[2:-1])
# prices = soup.find_all('span', {'class':"sp__product_description_content"})
prices = soup.find_all('span', attrs={"style":"font-size:14px;color:#555555;font-weight:bold;"})
f_prices = list()
for each in prices:
    if each.text.endswith('원') or each.text.endswith('원 '):
        f_prices.append(each.text)
# f_prices = f_prices[1:2] + f_prices[3:] 
print(len(f_prices))
print(len(f_titles))
# print(f_titles)
# print(f_prices)
result = dict(zip(f_titles, f_prices))

for each in result.items():
    print(each)