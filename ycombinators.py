from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
"""if we only print response we will only get the status code i.e 200 whereas response.text gives the whole html of page"""
# print(response.text)
yc_web_page = response.text

soup =  BeautifulSoup(yc_web_page, 'html.parser')
# print(soup)


link_and_title = soup.find_all(class_="titleline")
# print(link_and_title)

title=[]
link=[]
for tag in link_and_title:
    tag_a=tag.select_one(selector="span a")
    title.append(tag_a.getText())
    link.append(tag_a.get("href"))

upvote=[]
upvote_tag = soup.find_all(class_="score")
for tag in upvote_tag:
    value=tag.getText()
    upvote.append(value)

#getting only the numerical value of upvote
for i in range(len(upvote)):
    temp=upvote[i].split()[0]
    upvote[i]=int(temp)


print(title)
print(link)
print(upvote)

#finding the article with max upvotes
print("*******Aricle with the highest upvote is:********")
max_value = max(upvote)
max_index = upvote.index(max_value)
print(title[max_index],link[max_index],upvote[max_index],sep="\n")

# """to get text,link and upvote of only one"""
# link_and_title = soup.find(class_="titleline")
# like_tag= soup.find(class_="score")
# # print(link_and_title)
# # print("$")
# # print(like_tag)

# tag_a=link_and_title.select_one("span a")
# # print("$")
# # print(tag_a)
# text = tag_a.getText()
# link = tag_a.get("href")
# upvote = like_tag.getText()

# print(text,link,upvote,sep="\n")














