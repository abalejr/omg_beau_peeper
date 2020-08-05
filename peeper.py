import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.omgbeaupeep.com/comics/Avatar_The_Last_Airbender/001/1/"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')

all_imgs = soup.find_all('img')
for img in all_imgs:
    print(img.get('src'))