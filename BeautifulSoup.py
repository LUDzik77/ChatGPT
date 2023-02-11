# the script  write youdescriptions of the books in the chosen genre.
#Check it out!

import requests
from bs4 import BeautifulSoup

#basicu url #     url = "http://books.toscrape.com/"
#example          url = "https://books.toscrape.com/catalogue/category/books/science-fiction_16/"

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
categories_container = soup.find("ul", class_="nav nav-list")
categories = categories_container.find_all("li")

list_to_show = []
for category in categories:
    if category.a["href"] == "catalogue/category/books_1/index.html": continue
    category_name = category.a["href"][25:-11]
    category_url = "http://books.toscrape.com" + category.a["href"]
    #print(category_url)
    list_to_show.append(category_name.strip())
print("choose category")    
print(" ".join(list_to_show))
user_category = input(" > ")

url_with_category = url +  "catalogue/category/books/" + user_category +"/"
page = requests.get(url_with_category)
soup = BeautifulSoup(page.content, "html.parser")

book_containers = soup.find_all("article", class_="product_pod")

for book_container in book_containers:
    title = book_container.h3.a["title"]
    book_url = url_with_category + book_container.h3.a["href"]
    
    book_response = requests.get(book_url)
    book_soup = BeautifulSoup(book_response.content, "html.parser")
    
    description = book_soup.find("meta", attrs=
                                 {'name':'description'})['content']
    
    print("Title -->", title)
    print("Description -->", description)
    print("\n")
    
 