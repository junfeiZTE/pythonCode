import requests
import webbrowser
param={"wd":"python"}
r1=requests.get('http://www.baidu.com/s',params=param)
print(r1.url)
#webbrowser.open(r.url)

data={'firstname':'John','lastname':'Xiao'}
r2=requests.post('http://pythonscraping.com/pages/files/processing.php',data=data)
print(r2.url)
print(r2.text)

file={'uploadFile': open('D:\\1.png','rb')}
r3=requests.post('http://pythonscraping.com/files/processing2.php',files=file)
print(r3.text)

payload={'username':'John','password':'password'}
r4=requests.post('http://pythonscraping.com/pages/cookies/welcome.php',data=payload)
print(r4.cookies.get_dict())

r5=requests.get('http://pythonscraping.com/pages/cookies/profile.php',cookies=r4.cookies)
print(r5.text)

session=requests.Session()
payload1={'username':'Peter','password':'password'}
r6=session.post('http://pythonscraping.com/pages/cookies/welcome.php',data=payload1)
print(r6.cookies.get_dict())

r7=session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(r7.text)
