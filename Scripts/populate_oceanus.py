from pony.orm import *
import ast
import pdb
from flashtext import KeywordProcessor

db = Database()

db.bind('mysql', host='oceanus.cse.buffalo.edu', user='jlchugh',
        passwd='50335580', db='cse442_2022_spring_team_e_db')

# db.generate_mapping(create_tables=True)

with open("recipes.txt", "r") as file:
    for line in file:
        dict = ast.literal_eval(line)
        url = dict['url']

        # separate ingredients by '#'
        ingredient_list = dict['ingredients']

        keyword_processor = KeywordProcessor()  # case insensitive by default
        keyword_dictionary = {
        '': ['list', 'of', 'keywords', 'for', 'replacementWord1']}

        for ing in ingredient_list:
            # remove numbers and spaces
            ing = ''.join([i for i in ing if not i.isdigit()])
            ing = ing.replace(" ", "")

            # https://stackabuse.com/searching-and-replacing-words-in-python-with-flashtext/
            ing = ing.replace("", "")

        # separate directions by '#'
        direction_list = dict['directions']
        for direction in direction_list:
            continue

 # [{"url": url, "title": title, "ingredients": ingredients, "directions": directions}]


# if I feel like being an engineer, im positive we can do better than .replace.replace.replace
 def check_if_contains_common_substrings(input_string):
     pass
