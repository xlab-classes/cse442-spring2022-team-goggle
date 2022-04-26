from pony.orm import *
import ast
import pdb
from flashtext import KeywordProcessor
import pony.orm as pny

db = Database()

db.bind('mysql', host='oceanus.cse.buffalo.edu', user='jlchugh',
        passwd='50335580', db='cse442_2022_spring_team_e_db')

db.generate_mapping(create_tables=True)

with open("recipes.txt", "r") as file:
    for line in file:
        dict = ast.literal_eval(line)
        url = dict['url']
        title = dict['title']
        # separate directions by '#'
        direction_list = dict['directions']
        direction_string = ""
        for direction in direction_list:
            direction_string += direction + '#'

        for direction in direction_list:
            continue

        # separate ingredients by '#'
        ingredient_list = dict['ingredients']
        ingredient_string = ""
        for ingredient in ingredient_list:
            ingredient_string += ingredient + '#'

        # create the Recipe db entry
        with pny.db_session:
            new_recipe = Recipe(url=url, title=title, ingredients=ingredient_string, directions=direction_string)

        keyword_processor = KeywordProcessor()  # case insensitive by default
        keyword_dictionary = {
        '': ['tablespoons', 'tablespoon', 'cup', 'cups', 'oz', 'ounces','ounce', 'pieces', 'pieces', 'can', 'sprig']}
        keyword_processor.add_keywords_from_dict(keyword_dictionary)

        for ing in ingredient_list:
            # remove common useless words
            # https://stackabuse.com/searching-and-replacing-words-in-python-with-flashtext/
            pre_ing = keywordProcessor.replace_keywords(ing)
            # remove numbers, symbols, and spaces
            ing_to_add = ''.join([i for i in pre_ing if i.isalpha()])

            # create the ingredient db entry
            with pny.db_session:
                new_ingredient = Ingredient.select(lambda c: ing_to_add in c.name)
                if new_ingredient:
                    # add the recipe to the found ingredient
                    new_ingredient.recipes.add(new_recipe)
                else:
                    # create a new ingredient
                    new_ingredient = Ingredient(name=ing_to_add)
                    new_ingredient.recipes.add(new_recipe)
