# coding=utf-8

from urllib.request import urlopen
import re
import _thread
import time
from bs4 import BeautifulSoup

#https://www.liepin.com/zhaopin/?pageSize=40&curPage=1
count = 0
searchURL = "https://www.liepin.com/zhaopin/?pageSize=40&key=%E6%8A%80%E6%9C%AF%E6%96%87%E6%A1%A3%E5%B7%A5%E7%A8%8B%E5%B8%88&curPage=0"
searchPage = urlopen(searchURL)
html = searchPage.read()
soup = BeautifulSoup(html, 'html.parser')
searchText = re.compile("技术文档工程师")
list1=soup.findAll("h3", attrs={"title":searchText}) # to find all <div> with class "content-word" in html

for name in list1:
    count += 1
    link = name.find("a")
    print(link.get("href")) # to print every <a>.text in console

print("we found %d links." % count)
# url= "https://www.liepin.com/job/1927097061.shtml"
# page = urlopen(url) # open the website
# html = page.read() # read website content
# soup = BeautifulSoup(html, 'html.parser') # create a parser object
# list2=soup.findAll("h3", string="职位描述：") # to find all <div> with class "content-word" in html
#
# for name in list2:
#     dspt = name.find_next_sibling("div")
#     print(dspt.get_text()) # to print every <a>.text in console