#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = 0
    # iterate through ingredients and amounts
    for ingredient, amount in recipe.items():

        # if any amount required is greater than on-hand end loop and return 0
        if(ingredient not in ingredients or amount > ingredients[ingredient]):
            batches = 0
            break

        # if amount is equal, set batches to one
        elif(amount == ingredients[ingredient]):
            batches = 1

        # if amount is less, check limitations
        elif(amount < ingredients[ingredient]):
            if(batches == 1):
                pass
            else:
                if(batches != 0 and batches < ingredients[ingredient] // amount):
                    pass
                else:
                    batches = ingredients[ingredient] // amount

    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
