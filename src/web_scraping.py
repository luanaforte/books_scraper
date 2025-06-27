import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

current_page = 1
data = []
proceed = True
base_url = "https://books.toscrape.com/catalogue/"

while proceed:
    print("Currently scraping page:", current_page)

    url = f"https://books.toscrape.com/catalogue/page-{current_page}.html"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser", from_encoding="utf-8")

    if soup.title and "404" in soup.title.text:
        proceed = False
    else:
        all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for book in all_books:
            item = {}
            item['Title'] = book.find("img").attrs["alt"]
            item['Link'] = urljoin(base_url, book.find("a").attrs["href"])
            item['Price'] = book.find("p", class_="price_color").text
            item['Stock'] = book.find("p", class_="instock availability").text.strip()
            data.append(item)

        current_page += 1

df = pd.DataFrame(data)
df.to_csv("books_data.csv", index=False) # Salva os dados em um CSV
print("Web scraping concluído. Dados salvos em 'books_data.csv'.")