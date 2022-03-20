import scrape_foodnetwork_1
import scrape_the_pioneer_woman
# this file will run the scripts in the current folder and collect them in a text file
f = open("recipes.txt", "a")

# run the food network script
recipe_list = scrape_food_network_a()
for item in recipe_list:
    f.write(item)

recipe_list = scrape_pioneer_recipes()
for item in recipe_list:
    f.write(item)

f.close()
