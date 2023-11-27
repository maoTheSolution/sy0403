import requests
from bs4 import BeautifulSoup as bs

# Lat-Lon of New York
URL = "https://www.naver.com"
resp = requests.get(URL)
# print(resp.status_code)
# print(resp.text)
soup = bs(resp.content, "html.parser")
print(soup.a)
print(soup.find_all('div'))