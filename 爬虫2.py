from bs4 import BeautifulSoup
from urllib.request import urlopen

html=urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)
print("-------------------------")
soup=BeautifulSoup(html,features='html.parser')
print(soup.h1)
print("-------------------------")
print(soup.p)

all_href=soup.find_all('a')
print("-------------------------")
print(all_href)
all_href=[l['href'] for l in all_href]
print("-------------------------")
print(all_href)
