#!/usr/bin/python3
#スクレイピング

import urllib.request
from bs4 import BeautifulSoup
import os

class Scraper:
    
    def __init__(self, site):
        self.site = site
        
    def scrape(self):
        file_path = os.path.join("./", "scrape.txt")
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        with open(file_path, "w") as f:
            for tag in sp.find_all("a"):
                url = tag.get("href")
                if url == None:
                    continue
                if "html" in url:
                    f.write(url + "\n")
                    #print("\n" + url)
                
                
news = "https://news.yahoo.co.jp/"
Scraper(news).scrape()
