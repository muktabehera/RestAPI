# https://hacker-news.firebaseio.com/v0/topstories.json
# https://hacker-news.firebaseio.com/v0/item/25489298.json

import json
import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
res = requests.get(url)
print(type(res.text))
res1 = json.loads(res.text)
print(type(res1))

a = []
for i in range(0,5):
    a1 = res1[i]
    stra1 = str(a1)
    url2 = "https://hacker-news.firebaseio.com/v0/item/" + stra1 +".json"
    p = requests.get(url = url2)
    ptext = p.text
    ptextlist = json.loads(ptext)
    title  = ptextlist['title']
    urltitle = ptextlist['url']
    dicttitle = {}
    dicttitle['title'] = title
    dicttitle['url'] = urltitle
    a.append(dicttitle)

print(a)




