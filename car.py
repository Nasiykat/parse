import requests
from bs4 import BeautifulSoup
import csv

URL = "https://cars.kg/offers/?vendor=57fa24ee2860c45a2a2c093b"
HEADERS = {
    "user-agent": "Mozilla/5.0 Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "accept": "*/*",
}
LINK = "https://cars.kg/"
FILE = "cars.csv"


def get_html(headers, url, params=None):
    response = requests.get(url, params=params, headers=headers)
    return response


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("a", class_="catalog-list-item")
    cars = []
    for i in items:
        cars.append({
            "title": i.find("span",class_="catalog-item-caption").get_text(),
            "image": i.find("img").get('src'),
            "description": i.find("span", class_="catalog-item-caption").get_text().replace("\n\n",""),
            "price": i.find("span", class_="catalog-item-price").get_text().replace("\n",""),

        })
    print(cars)
    return cars


def save_file(content, file):
    with open(file, "w") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(["Название продукта", "Картинка", "Описание",  "Цена"])
        for i in content:
            writer.writerow([i['title'], i['image'], i['description'], i['price']])


def get_parse_result():
    html = get_html(url=URL, headers=HEADERS)
    # print(html.text)
    content = get_content(html.text)
    save_file(content, FILE)


get_parse_result()

