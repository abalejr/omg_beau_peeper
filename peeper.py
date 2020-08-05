import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from urllib import urlopen
from bs4 import BeautifulSoup

url = "https://www.omgbeaupeep.com/comics/Avatar_The_Last_Airbender/001/1/"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')


print(soup.title)

# urllib.urlretrieve("https://www.omgbeaupeep.com/comics/mangas/Avatar%20The%20Last%20Airbender/001%20-%20Avatar%20The%20Last%20Airbender%20-%20The%20Promise%20Part%201%20(2012)/read-avatar-the-last-airbender-comics-online-free-001.jpg", "page1.jpg")