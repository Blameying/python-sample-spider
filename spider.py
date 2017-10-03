from lxml import etree
import requests
from tkinter import *

root = Tk(screenName=None, baseName=None, className='Tk', useTk=1)
root.title("News")

label = Label(root, text="Waiting!", bg='black', fg='#ADFF2F')
label.pack(fill=X)

req = requests.Session()
req.headers.clear()
text = req.get('http://today.hitwh.edu.cn/news_more_list.asp?id=7')
text.encoding = 'utf-8'
html = etree.HTML(text.text)

results = html.xpath("//li/a[@target='_blank']")
count = html.xpath("//li//span/font")
date = html.xpath("//div/ul/li/font")

strs = []

for i in range(len(date)):
    strs.append(date[i].text + '\n' + results[i].text + '\n' + count[i].text)

for i in range(3):
    label = Label(root, text=strs[i], bg='black', fg='#ADFF2F')
    label.pack(fill=X)


root.mainloop()
# print(text.text)
