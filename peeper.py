from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from PIL import Image

#Set variables for the base page of the comic
#Change the url to the base url of the comic with no page number, be sure to include a trailing /
url = "https://www.omgbeaupeep.com/comics/Avatar_The_Last_Airbender/003/"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')

#Find the dropdown for the page selector to use to set the page number
comic_pager = soup.find('select', {"name": "page"})
comic_pages = comic_pager.findChildren()
#Initialize page_list variable as an empty array
page_list = []

#Foop through the page numbers, download the page, and generate a list of Image objects
for page in comic_pages:
    #Set variable for this particular page
    page_num = page.get('value')
    page_url = url + page_num
    page_html = urlopen(page_url)
    page_soup = BeautifulSoup(page_html, 'lxml')

    #Find the page and set variables for the name of the file and the src of the page
    page_img = page_soup.find('img', {"class": "picture"})
    page_relative_src = page_img.get('src')
    page_src = "https://www.omgbeaupeep.com/comics/" + page_relative_src
    encoded_page_src = page_src.replace(" ", "%20")
    jpg_name = f"jpgs/page{page_num}.jpg"

    #Download the page
    urlretrieve(encoded_page_src, jpg_name)

    #Create an Image object and append it to the page_list array
    jpg = Image.open(jpg_name)
    page_list.append(jpg)

#Define the first page of the comic, then delete it from the array
page_1 = page_list[0]
del page_list[0]

#Convert the first page to a pdf with all the other images appended to it as additional pages
page_1.save("comic.pdf", "PDF", resolution=100.0, save_all=True, append_images=page_list)
