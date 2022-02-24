from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests

sitemap_xml ="https://www.therecipedepository.com/site-map/categories"
sitemap_response = requests.get(sitemap_xml)

# note page.content is raw (thats why we arent using page.text)
soup = BeautifulSoup(sitemap_response.content, "html.parser")

category_urls = soup.findAll("url")
category_urls = [category_url.find("loc").string for category_url in category_urls]

recipe_urls = []
for category_url in category_urls:
    new_links_in_category = []
    print("processing \"" + category_url + "\"")
    # get request to the page
    page = requests.get(category_url)

    # load it into BeautifulSoup
    soup = BeautifulSoup(page.content, "html.parser")

    # select the recipe item elements
    recipes = soup.select("[class~=recipe-item]")

    # collect the link in the
    for recipe_link in recipes:
        new_links_in_category = recipe_link.get('href')

    # add the links to the collection of links
    recipe_urls = recipe_urls + new_links_in_category

    print(new_links_in_category)
