import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from PIL import Image

url = "https://www.omgbeaupeep.com/comics/Avatar_The_Last_Airbender/001/"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')

comic_pager = soup.find('select', {"name": "page"})
comic_pages = comic_pager.findChildren()
comic_length = len(comic_pages)
for page in comic_pages:
    page_num = page.get('value')
    page_url = url + page_num
    page_html = urlopen(page_url)
    page_soup = BeautifulSoup(page_html, 'lxml')

    page_img = page_soup.find('img', {"class": "picture"})
    page_relative_src = page_img.get('src')
    page_src = "https://www.omgbeaupeep.com/comics/" + page_relative_src
    encoded_page_src = page_src.replace(" ", "%20")
    
    urlretrieve(encoded_page_src, f"jpgs/page{page_num}.jpg")
