IMAGE_URL="https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
from urllib.request import urlretrieve
urlretrieve(IMAGE_URL,'D:\\Python36-32\菜鸟\learn.png')

import requests
r=requests.get(IMAGE_URL)
with open('D:\\Python36-32\菜鸟\learn1.png','wb') as f:
    f.write(r.content)

r1=requests.get(IMAGE_URL,stream=True)
with open('D:\\Python36-32\菜鸟\learn2.png','wb') as f:
    for chunk in r1.iter_content(chunk_size=32):
        f.write(chunk)
    
