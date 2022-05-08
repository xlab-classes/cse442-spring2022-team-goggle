from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import pdb

# returns a list of dictionaries in the form {"title": title, "ingredients": ingredients, "instructions": instructions}
# where ingredients, and instructions are lists of strings and title is a string

def scrape_food_network_a():
    print("food network")
    recipes = []

    with open('../Data/foodnetwork1.xml', 'r') as f:
        data = f.read()

    Bs_data = BeautifulSoup(data, "lxml")
    b_unique = Bs_data.find_all('url')

    recipe_links = []
    for b in b_unique:
        try:
            if "/recipes/" in str(b.find("loc")):
                # remove <loc> and </loc> (im lazy)
                recipe_links += [str(b.find("loc"))[5:-6]]
        except: continue
    #sz = str(len(recipe_links))
    #i = 0
    for url in recipe_links:
        try:
            print("hi")
            #print(str(i) + " / " + sz )
            #i += 1

            get = requests.get(url)
            soup = BeautifulSoup(get.content, "html.parser")

            # get the title
            title = soup.find_all(class_="o-AssetTitle__a-HeadlineText")[0].text
            # get the ingredients
            ingredient_elements = soup.find_all(class_="o-Ingredients__a-Ingredient--Checkbox")
            ingredients = list(map(lambda x: x["value"], ingredient_elements))
            if len(ingredients) == 0: continue
            ingredients.pop(0)

            # get the directions
            direction_elements = soup.find_all(class_="o-Method__m-Step")
            directions = list(map(lambda x: x.text.strip().replace('\xa0', ' '), direction_elements))
            if len(directions) == 0: continue


            recipes += [{"url": url, "title": title, "ingredients": ingredients, "directions": directions}]
        except: continue
    return recipes
