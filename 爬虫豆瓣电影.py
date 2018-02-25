import requests
import bs4

def open_url(url):
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    res=requests.get(url,headers=headers)
    soup=bs4.BeautifulSoup(res.text,"html.parser")
    return soup

def find_movie(soup):
    #movie name
    targets=soup.find_all("div",{"class":"hd"})
    res=[]
    for each in targets:
        #print(each.a.span.text)
        res.append(each.a.span.text)

    #movie rating
    targets_ra=soup.find_all("span",{"class":"rating_num"})
    res_ra=[]
    for each in targets_ra:
        #print(each.text)
        res_ra.append(each.text)

    ret=[]
    for i in range(len(res)):
        ret.append(res[i]+"**"+res_ra[i])
    return ret


host="https://movie.douban.com/top250?start="
host0="https://movie.douban.com/top250"
res=requests.get(host0)
soup=bs4.BeautifulSoup(res.text,"html.parser")
depth=soup.find('span',{"class":"next"}).previous_sibling.previous_sibling.text
print(depth)

result=[]
for i in range(int(depth)):
    url=host+str(25*i)
    res=open_url(url)
    result.extend(find_movie(res))

print(result)
print(len(result))
