from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv

scrapepage = requests.get("https://www.nike.com/w/womens-shoes-5e1x6zy7ok")
soup = BeautifulSoup(scrapepage.text, "html.parser")

file = open("scraper.csv", "a")
writer = csv.writer(file)

writer.writerow(["SHOES", "PRICES"])

shoenames = soup.findAll("a", attrs={"class": "product-card__link-overlay"})
prices = soup.findAll("div", attrs={"class": "product-price us__styling is--current-price css-11s12ax"})
# authors = soup.findAll("div", attrs={"class": "author"})

for shoename, price in zip(shoenames, prices):
    print(shoename.text + "-" + price.text)
    writer.writerow([shoename.text, price.text])
file.close()

