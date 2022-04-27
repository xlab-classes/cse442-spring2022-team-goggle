from flask import Flask

import pdb

saved_recipes = []
recipes = []
ingredients = []


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jflsiejwlkjsdf'

    from .views import views
    from .auth import auth
    from .models import User, Ingredient, Recipe
    create_model_data()
    # register the views
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app


def create_model_data():
    global saved_recipes
    global ingredients
    global recipes
    from .models import User, Ingredient, Recipe
    # create some recipes
    hamburger = Recipe(title="hambuger",
                       url="https://www.foodnetwork.com/recipes/food-network-kitchen/hamburgers-recipe2-2040357",
                       ingredients=['ground chuck', 'salt', 'pepper', 'vegetable oil',
                                    'cheddar cheese', 'buns', 'lettuce', 'tomatoes'],
                       directions=["Preheat the oven to 450 degrees F. Place a roasting rack on a foil-lined baking sheet in the oven.", "Using your hands, break the meat into small pieces and combine evenly but loosely on a parchment or waxed paper-lined baking sheet. Spread the meat out and season it generously with salt and pepper. If desired, add the spice mix at this time.", "Divide the meat into 4 portions (about 6 ounces each). Using your hands, form each portion into a ball-shape by gently tossing it from 1 hand to the other. (Don't over work or press too firmly on the meat.) Gently form each portion into a patty about 3 1/2 inches wide and 1-inch-thick. ", "Preheat a large cast iron skillet over medium-low heat for 5 minutes. Raise the heat to high and add the oil. Add the patties and cook, turning once, until well-browned, about 2 minutes each side.", "Using a spatula, transfer the hamburgers to the roasting rack in the oven and continue cooking to desired doneness, 8 to 9 minutes for medium-rare, 10 to 11 minutes for medium, and 13 to 15 minutes for well-done. If you are using the cheese, top the hamburgers during their last couple of minutes of cooking to melt. ", "Transfer the hamburgers to a plate, let rest for a couple minutes before serving. Meanwhile, toast the hamburger buns. Assemble the hamburgers with the condiments and toppings of your choice. Serve.", "For Medium-Rare: Cook for 3 minutes covered and then unplug the machine and continue to cook covered for 2 to 3 more minutes. "])
    grilled_cheese = Recipe(title="The Perfect Grilled Cheese",
                            url="https://www.foodnetwork.com/recipes/food-network-kitchen/the-perfect-grilled-cheese-3636831",
                            ingredients=["cheddar cheese",
                                         "bread", "mayonnaise"],
                            directions=["Oven method (great for a crowd of six or fewer): Put a rimmed baking sheet on the middle rack of the oven and preheat to 450 degrees F. Make one sandwich per person: Sandwich 2 slices of cheese between 2 slices of bread. Spread or brush the outside of the sandwich with 1 tablespoon of fat. Place on the preheated baking sheet and cook until the cheese starts to melt, about 5 minutes. Flip the sandwich and bake until golden brown, an additional 5 minutes.", "Panini press method (for crispy crunchy sandwich that needs minimal attention): Sandwich 2 slices of cheese between 2 slices of bread. Preheat a panini press to medium heat. Spread or brush the outside of the sandwich with 1 tablespoon of fat and place in the press. Close the top and cook until lightly browned and the cheese is melted, 5 to 6 minutes.  ", "Skillet method (fool-proof and low-tech): Sandwich 2 slices of cheese between 2 slices of bread. Preheat a skillet over medium-low heat. Spread or brush the outside of the sandwich with 1 tablespoon of fat and cook until lightly browned, 3 to 4 minutes. Flip the sandwich, and continue cooking until browned and the cheese is melted, 3 to 4 minutes more. "])
    burger_sandwich = Recipe(title="burger sandwich",
                             url="burgersandwich.com", ingredients=["cheddar cheese",
                                                                    "bread", "mayonnaise", "ground chuck"],
                             directions=["cook the ground chuck to safe temperature", "butter and toast the bread", "apply cheese and toast for 3 minutes or until cheese is melted", "add condiments"])

    recipes = [hamburger, grilled_cheese, burger_sandwich]

    ingredients += [Ingredient(name="ground chuck", recipes=[hamburger, burger_sandwich])]
    ingredients += [Ingredient(name="cheddar cheese", recipes=[hamburger, burger_sandwich, grilled_cheese])]
    ingredients += [Ingredient(name="bread", recipes=[burger_sandwich, grilled_cheese])]

    saved_recipes = [grilled_cheese]
