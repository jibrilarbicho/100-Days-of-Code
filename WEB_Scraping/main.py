from bs4 import BeautifulSoup
from certifi import contents

with open("/home/jibril/Documents/Python/WEB_Scraping/website.html") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")
all_anchor_tag = soup.findAll(name="a")
for anch in all_anchor_tag:
    print(anch.getText())
heading = soup.find(name="h1", id="name")
print(heading)
headings = soup.select(".heading")
print("headings", headings)
