import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

url = "https://www.omgbeaupeep.com/comics/Avatar_The_Last_Airbender/001/1/"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')

page = soup.find_all('img', {"class": "picture"})[0]
page_relative_src = page.get('src')

page_src = "https://www.omgbeaupeep.com/comics/" + page_relative_src
encoded_page_src = page_src.replace(" ", "%20")

urlretrieve(encoded_page_src, "page1.jpg")