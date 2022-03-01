from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import pdb

sitemap_xml ="https://www.therecipedepository.com/site-map/categories"
sitemap_response = requests.get(sitemap_xml)

# note page.content is raw (thats why we arent using page.text)
soup = BeautifulSoup(sitemap_response.content, "html.parser")

category_urls = soup.findAll("url")
category_urls = [category_url.find("loc").string for category_url in category_urls]

recipe_urls = []
for category_url in category_urls:
    print("-----------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------")
    print("processing \"" + category_url + "\"")
    print("-----------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------")
    # get request to the page
    page = requests.get(category_url)

    # load it into BeautifulSoup
    soup = BeautifulSoup(page.content, "html.parser")
    recipes_from_id = soup.find(id='recipes')
    recipe_items = recipes_from_id.find_all(class_='recipe-item') if recipes_from_id is not None else []

    # for each recipe html chunk: for each a: a['href'] is the suffix
    for item in recipe_items:
        for a in item.find_all('a'):
            recipe_urls.append("https://www.therecipedepository.com" + a['href'])
    for url in recipe_urls:
        print(url)
    print()
print("Done")
