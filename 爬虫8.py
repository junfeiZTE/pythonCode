from bs4 import BeautifulSoup
import requests

URL="http://www.nationalgeographic.com.cn/animals/"

html=requests.get(URL).text
soup=BeautifulSoup(html,'html.parser')
img_ul=soup.find_all('ul',{"class":"img_list"})

print(img_ul)
print(len(img_ul))


for ul in img_ul:
    imgs=ul.find_all('img')
    print("------------------")
    print(imgs)
    print("------------------")
    for img in imgs:
        url=img['src']
        r=requests.get(url,stream=True)
        image_name=url.split('/')[-1]
        with open('D:\\Python36-32\菜鸟\%s'%image_name,'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)
