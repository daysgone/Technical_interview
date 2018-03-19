'''
def groupingDishes(dishes):
    """ Group dishes by ingredients
        - only list if ingredient is in at list 2 dishes
        - first element in list is the nameof the ingredient
        - all other elements in list are the names of the dishes that contain this ingredient
        - sorted in lexographical order by names
    """
    by_ingredients = {}

    for dish in dishes:
        for ingredient in dish[1:]:
            if ingredient in by_ingredients:
                by_ingredients[ingredient].append(dish[0])
            else:
                by_ingredients[ingredient] = [dish[0]]

    new_grouping = []

    for key in sorted(by_ingredients.keys()):
        if len(by_ingredients[key]) > 1:
            new_list = sorted(by_ingredients[key])
            new_list.insert(0,key)
            #print new_list
            new_grouping.append(new_list)
    #print new_grouping
    return new_grouping
'''


def groupingDishes(dishes):
    """ Group dishes by ingredients
        - only list if ingredient is in at list 2 dishes
        - first element in list is the nameof the ingredient
        - all other elements in list are the names of the dishes that contain this ingredient
        - sorted in lexographical order by names
    """
    by_ingredients = {}
    for dish in dishes:
        for ingredient in dish[1:]:
            if ingredient in by_ingredients:
                by_ingredients[ingredient].append(dish[0])
            else:
                by_ingredients[ingredient] = [dish[0]]

    new_grouping = []

    for ingredient in sorted(by_ingredients):
        if len(by_ingredients[ingredient]) > 1:
            new_grouping.append([ingredient] + sorted(by_ingredients[ingredient]))
    return new_grouping