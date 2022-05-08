from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import pdb

# returns a list of dictionaries in the form {"title": title, "ingredients": ingredients, "instructions": instructions}
# where ingredients, and instructions are lists of strings and title is a string


def scrape_pioneer_recipes():
    print("woman")
    recipes = []

    with open('../Data/pioneer_data.xml', 'r') as f:
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

            #print(str(i) + " / " + sz )
            #i+=1

            get = requests.get(url)
            soup = BeautifulSoup(get.content, "html.parser")

            if  bool(soup.find_all(class_="recipe-hed")[0].text):
                title = soup.find_all(class_="recipe-hed")[0].text
            else:
                continue
            ingredients = []

            ingredients_elems = soup.find_all(class_="ingredient-item")

            for ingredient in ingredients_elems:
                if bool(ingredient.find_all(class_="ingredient-amount")):
                    # i am so sorry if you are reading this
                    # we are just splitting to remove whitespace chars and then joining it with " "'s in between
                    amount = " ".join(ingredient.find_all(class_="ingredient-amount")[0].text.split())
                    ingre = " ".join(ingredient.find_all(class_="ingredient-description")[0].text.split())
                    ing_string =  amount + " " + ingre
                else:
                    ing_string = ingredient.find_all(class_="ingredient-description")[0].text.strip()

                if ing_string not in ingredients:
                    ingredients += [ing_string]


            directions_elem = soup.find_all(class_="direction-lists")[0]
            direction_elems = directions_elem.find_all('li')

            directions = []
            # remove the li
            for elem in direction_elems:
                directions += [elem.text.strip().replace('\xa0', ' ')]

            recipes += [{"url": url, "title": title, "ingredients": ingredients, "directions": directions}]
        except: continue


    return recipes
