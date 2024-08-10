from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import io
from PIL import Image
from pathlib import Path
import hashlib

def get_all_site(link):
    options = ChromeOptions()
    options.add_argument("--headless=new")
    scraper = webdriver.Chrome(options=options)

    scraper.get(link)
    site = scraper.page_source
    soup = BeautifulSoup(site, "html.parser")

    def parse_text(location, classes):
        return soup.findAll(f"{location}", attrs={"class": f"{classes}"})

    shoenames = parse_text("p","chakra-text css-1lnwi02")
    prices = parse_text("p","chakra-text css-sk35rx")

    def parse_img_urls(classes, location, src):
        results = []
        for a in soup.findAll(attrs={"class":classes}):
            name = a.find(location)
            if name not in results:
                results.append(name.get(src))
        return results

    parse_img_urls("css-tkc8ar", "img", "src")

    file = open("stockx.csv", "a")
    writer = csv.writer(file)

    returned_results = parse_img_urls("css-tkc8ar", "img", "src")

    for shoename, price, link in zip(shoenames, prices, returned_results):
        # print(shoename.text + " - " + price.text + " - " + link)
        writer.writerow([shoename.text, price.text, link])

    file.close()

    # for x in returned_results:
    #     imgcontent = requests.get(x).content
    #     imgfile = io.BytesIO(imgcontent)
    #     image = Image.open(imgfile).convert("RGB")
    #     file_path = Path("test", hashlib.sha1(imgcontent).hexdigest()[:10] + ".png")
    #     image.save(file_path, "PNG", quality=80)

    scraper.quit()

urllist = ['https://stockx.com/browse/men?page=1', 'https://stockx.com/browse/men?page=2', 'https://stockx.com/browse/men?page=3', 'https://stockx.com/browse/men?page=4', 'https://stockx.com/browse/men?page=5', 'https://stockx.com/browse/men?page=6', 'https://stockx.com/browse/men?page=7', 'https://stockx.com/browse/men?page=8', 'https://stockx.com/browse/men?page=9', 'https://stockx.com/browse/men?page=10', 'https://stockx.com/browse/men?page=11', 'https://stockx.com/browse/men?page=12', 'https://stockx.com/browse/men?page=13', 'https://stockx.com/browse/men?page=14', 'https://stockx.com/browse/men?page=15', 'https://stockx.com/browse/men?page=16', 'https://stockx.com/browse/men?page=17', 'https://stockx.com/browse/men?page=18', 'https://stockx.com/browse/men?page=19', 'https://stockx.com/browse/men?page=20', 'https://stockx.com/browse/men?page=21', 'https://stockx.com/browse/men?page=22', 'https://stockx.com/browse/men?page=23', 'https://stockx.com/browse/men?page=24', 'https://stockx.com/browse/men?page=25']

for x in range(25):
    get_all_site(urllist[x])
