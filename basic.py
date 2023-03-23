# step2
from bs4 import BeautifulSoup

# Step1
with open("website.html","r", encoding="utf-8") as file:
    contents = file.read()

# step3
# Now the soup will act as a object and we can access all the tag's like we access variable of a object
soup = BeautifulSoup(contents, 'html.parser')

#accessing a tag like a object's variable
print(soup.title)

#Always get's the first occurence
# print(soup.a)
# print(soup.ul)

#to find all same tag in a file
all_anchor_tag = soup.find_all(name="a")
all_anchor_tag = soup.find_all(name="a", id="name")

for tag in all_anchor_tag:
# to extract text from a tag
    print(tag.getText())

for tag in all_anchor_tag:
    print(tag.get("href"))


#CSS selectors

web_url = soup.select_one(selector="p a")
print(web_url)

name = soup.select_one(selector="#name")
print(name)

heading = soup.select(selector=".heading")
print(heading)