from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests

# returns a list of dictionaries in the form {"title": title, "ingredients": ingredients, "instructions": instructions}
# where ingredients, and instructions are lists of strings and title is a string


def scrape_pioneer_recipes():
    recipes = []

    with open('../Data/pioneer_data.xml', 'r') as f:
        data = f.read()

    Bs_data = BeautifulSoup(data, "xml")
    b_unique = Bs_data.find_all('url')

    recipe_links = []
    for b in b_unique:
        if "cooking-tips-tutorials" in str(b.find("loc")) or "/recipes/" in str(b.find("loc")):
            # remove <loc> and </loc> (im lazy)
            recipe_links += [str(b.find("loc"))[5:-6]]

    for url in recipe_links:
        get = requests.get(url)
        soup = BeautifulSoup(get.content, "html.parser")
        # if url is recipe

        # if url in cooking-tips-tutorials

        # gonna need to catch all errors :| ... >:)

scrape_pioneer_recipes()
