import requests
from bs4 import BeautifulSoup as bs


url = 'https://testmoa.com/mbti-compatibility/'
page = requests.get(url)
soup = bs(page.text, "html.parser")


# for each in soup.find_all('h3',{'class':'wp-block-heading'}):
    # print(each.text)
for each in soup.find_all('figure', {'wp-block-table aligncenter is-style-stripes'}):
    print(each.text[:4])
    # 최고의 궁합
    print("최고의 궁합 : ", [e.text for e in each.find_all('td')[3] if e.text != ', ' and e.text != ',\xa0'])
    # 좋은 궁합
    print("좋은 궁합 : ", [e.text for e in each.find_all('td')[5] if e.text != ', ' and e.text != ',\xa0'])
    # 최악의 궁합
    print("최악의 궁합 : ", [e.text for e in each.find_all('td')[7] if e.text != ', ' and e.text != ',\xa0'])
    print("*"*10)