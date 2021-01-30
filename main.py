import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd

temp_dict = {
    "title": [],
    "article-nr": [],
    "dimensions": [],
    "price": []
}


my_url = "https://www.mediamarkt.ch/de/category/_tv-fernseher-61-bis-70-zoll-680942.html"

#Opening up connection
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#HTML parsing
page_soup = soup(page_html, "html.parser")


temp_containers = page_soup.findAll("div", {"class": "product-wrapper"})
print(len(temp_containers))


dimensions = 0


for container in temp_containers:

    content = container.find("div", {"class": "content"})

    temp_dict["title"].append(content.h2.a.text.strip())

    temp_dict["article-nr"].append(content.div.text)

    temp_dict["price"].append(container.find("div", {"class": "price small"}).text)



    for i in content.find_all("dd"):


        if "cm" in i.text:

            temp_dict["dimensions"].append(i.text)

        counter = +1

data_dict = pd.DataFrame(temp_dict)

data_dict.to_csv('script_data.csv', index=False)