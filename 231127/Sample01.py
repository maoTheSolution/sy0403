import requests as req
from bs4 import BeautifulSoup as bs


url = 'https://www.puppydog.co.kr'
op = '/category/고양이간식/116/'
res = req.get(url+op,  headers={"User-Agent": "Safari 17.1"})
soup = bs(res.text, "html.parser")
# soup.prettify()
for each in soup.find_all('div', {'class':'sp__product_title_247'}):
    print(each.text)