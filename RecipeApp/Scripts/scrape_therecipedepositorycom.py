from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests

sitemap_xml ="https://www.therecipedepository.com/site-map/categories"
sitemap_response = requests.get(sitemap_xml)

# note page.content is raw (thats why we arent using page.text)
soup = BeautifulSoup(sitemap_response.content, "html.parser")

category_urls = soup.findAll("url")
category_urls = [category_url.find("loc").string for category_url in category_urls]

for category_url in category_urls:
    print("processing \"" + url + "\"")
    page = requests.get(category_url)
