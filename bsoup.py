import requests
from bs4 import BeautifulSoup



page =requests.get('https://timesofindia.indiatimes.com/life-style/books/features/Mahakavi-Bharathiyar-an-inspiration-to-everyone/articleshow/27211482.cms')
soup = BeautifulSoup(page.content, 'html.parser')    

#print(soup)

'''
    class = .
    id = #
'''


div_tags = soup.select("div.Normal em")

#print(div_tags)

for dts in div_tags:
    print(dts.text)