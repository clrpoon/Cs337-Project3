import copy
import re
from ingredient import *

from RecipeFetcher import *
# COOKING_METHOD_TO_SUBSTITUTE = { #TODO: add shellfish
# """
# 'liver': 'tofu',
#
#     'quail': 'eggplant',
#     'rabbit': 'beans',
#     'pheasant': 'eggplant',
#     'goose': 'eggplant',
#
#
# """
#     'boil':{
#         'chicken': 'tofu',
#         'turkey': 'tofu',
#         'beef': 'mushroom',
#         'lamb': 'mushroom',
#         'pork': 'mushroom',
#         'fish': 'tofu',
#         'ground': 'beans',
#         'ham': 'tempeh',
#         'liver': 'tofu',
#         'ribs': 'tempeh',
#         'bacon': 'vegetarian bacon',
#         'sausage': 'tofu',
#         'veal': 'seitan',
#         'carp': 'lentils',
#         'catfish': 'lentils',
#         'salmon': 'lentils',
#         'tilapia': 'lentils',
#         'tuna': 'lentils',
#         'trout': 'lentils',
#         'crayfish': 'lentils',
#         'lobster': 'lentils',
#         'shrimp': 'lentils',
#         'prawns': 'lentils',
#         'oyster': 'lentils',
#         'mussel': 'lentils',
#         'clams': 'lentils'
#     },
#     'bake':{
#         'chicken': 'seitan',
#         'turkey': 'mushroom',
#         'beef': 'mushroom',
#         'lamb': 'mushroom',
#         'pork': 'mushroom',
#         'fish': 'tempeh',
#         'ground': 'beans',
#         'ham': 'tempeh',
#         'liver': 'tofu',
#         'bacon': 'vegetarian bacon',
#         'sausage': 'tofu',
#         'veal': 'seitan',
#         'carp': 'lentils',
#         'catfish': 'lentils',
#         'salmon': 'lentils',
#         'tilapia': 'lentils',
#         'tuna': 'lentils'
#         'trout': 'lentils',
#         'crayfish': 'lentils',
#         'lobster': 'lentils',
#         'shrimp': 'lentils',
#         'prawns': 'lentils',
#         'oyster': 'lentils',
#         'mussel': 'lentils',
#         'clams': 'lentils'
#     },
#     'simmer':{
#         'chicken': 'tofu',
#         'turkey': 'tofu',
#         'beef': 'mushroom',
#         'lamb': 'mushroom',
#         'pork': 'jackfruit',
#         'fish': 'tofu',
#         'ground': 'beans',
#         'ham': 'tempeh',
#         'liver': 'tofu',
#         'bacon': 'vegetarian bacon',
#         'sausage': 'tofu',
#         'veal': 'seitan',
#         'carp': 'lentils',
#         'catfish': 'lentils',
#         'salmon': 'lentils',
#         'tilapia': 'lentils',
#         'tuna': 'lentils'
#         'trout': 'lentils',
#         'crayfish': 'lentils',
#         'lobster': 'lentils',
#         'shrimp': 'lentils',
#         'prawns': 'lentils',
#         'oyster': 'lentils',
#         'mussel': 'lentils' ,
#         'clams': 'lentils'
#     },
#     'roast':{
#         'chicken': 'tofu',
#         'turkey': 'tofu',
#         'beef': 'mushroom',
#         'lamb': 'mushroom',
#         'pork': 'jackfruit',
#         'fish': 'tofu',
#         'ground': 'beans',
#         'ham': 'tempeh',
#         'liver': 'tofu',
#         'bacon': 'vegetarian bacon',
#         'sausage': 'tofu',
#         'veal': 'seitan',
#         'carp': 'lentils',
#         'catfish': 'lentils',
#         'salmon': 'lentils',
#         'tilapia': 'lentils',
#         'tuna': 'lentils'
#         'trout': 'lentils',
#         'crayfish': 'lentils',
#         'lobster': 'lentils',
#         'shrimp': 'lentils',
#         'prawns': 'lentils',
#         'oyster': 'lentils',
#         'mussel': 'lentils' ,
#         'clams': 'lentils'
#     },
#     'fry':{
#         'chicken': 'tofu',
#         'turkey': 'tofu',
#         'beef': 'mushroom',
#         'lamb': 'mushroom',
#         'pork': 'jackfruit',
#         'fish': 'tofu',
#         'ground': 'beans',
#         'ham': 'tempeh',
#         'liver': 'tofu',
#         'bacon': 'vegetarian bacon',
#         'sausage': 'tofu',
#         'veal': 'seitan',
#         'carp': 'lentils',
#         'catfish': 'lentils',
#         'salmon': 'lentils',
#         'tilapia': 'lentils',
#         'tuna': 'lentils'
#         'trout': 'lentils',
#         'crayfish': 'lentils',
#         'lobster': 'lentils',
#         'shrimp': 'lentils',
#         'prawns': 'lentils',
#         'oyster': 'lentils',
#         'mussel': 'lentils' ,
#         'clams': 'lentils'
#     },
#     'deep fry':{
#         'chicken': 'tofu',
#         'turkey': 'tofu',
#         'beef': 'mushroom',
#         'lamb': 'mushroom',
#         'pork': 'jackfruit',
#         'fish': 'tofu',
#         'ground': 'beans',
#         'ham': 'tempeh',
#         'liver': 'tofu',
#         'bacon': 'vegetarian bacon',
#         'sausage': 'tofu',
#         'veal': 'seitan',
#         'carp': 'lentils',
#         'catfish': 'lentils',
#         'salmon': 'lentils',
#         'tilapia': 'lentils',
#         'tuna': 'lentils'
#         'trout': 'lentils',
#         'crayfish': 'lentils',
#         'lobster': 'lentils',
#         'shrimp': 'lentils',
#         'prawns': 'lentils',
#         'oyster': 'lentils',
#         'mussel': 'lentils' ,
#         'clams': 'lentils'
#     },
#     'deep-fry':{
#         'chicken': 'tofu',
#         'turkey': 'tofu',
#         'beef': 'mushroom',
#         'lamb': 'mushroom',
#         'pork': 'jackfruit',
#         'fish': 'tofu',
#         'ground': 'beans',
#         'ham': 'tempeh',
#         'liver': 'tofu',
#         'bacon': 'vegetarian bacon',
#         'sausage': 'tofu',
#         'veal': 'seitan',
#         'carp': 'lentils',
#         'catfish': 'lentils',
#         'salmon': 'lentils',
#         'tilapia': 'lentils',
#         'tuna': 'lentils'
#         'trout': 'lentils',
#         'crayfish': 'lentils',
#         'lobster': 'lentils',
#         'shrimp': 'lentils',
#         'prawns': 'lentils',
#         'oyster': 'lentils',
#         'mussel': 'lentils' ,
#         'clams': 'lentils'
#     },
#     'stiry fry':{
#         'chicken': 'tofu',
#         'turkey': 'tofu',
#         'beef': 'mushroom',
#         'lamb': 'mushroom',
#         'pork': 'jackfruit',
#         'fish': 'tofu',
#         'ground': 'beans',
#         'ham': 'tempeh',
#         'liver': 'tofu',
#         'bacon': 'vegetarian bacon',
#         'sausage': 'tofu',
#         'veal': 'seitan',
#         'carp': 'lentils',
#         'catfish': 'lentils',
#         'salmon': 'lentils',
#         'tilapia': 'lentils',
#         'tuna': 'lentils'
#         'trout': 'lentils',
#         'crayfish': 'lentils',
#         'lobster': 'lentils',
#         'shrimp': 'lentils',
#         'prawns': 'lentils',
#         'oyster': 'lentils',
#         'mussel': 'lentils' ,
#         'clams': 'lentils'
#     },
#     'stir-fry':{
#         'chicken': 'tofu',
#         'turkey': 'tofu',
#         'beef': 'mushroom',
#         'lamb': 'mushroom',
#         'pork': 'jackfruit',
#         'fish': 'tofu',
#         'ground': 'beans',
#         'ham': 'tempeh',
#         'liver': 'tofu',
#         'bacon': 'vegetarian bacon',
#         'sausage': 'tofu',
#         'veal': 'seitan',
#         'carp': 'lentils',
#         'catfish': 'lentils',
#         'salmon': 'lentils',
#         'tilapia': 'lentils',
#         'tuna': 'lentils'
#         'trout': 'lentils',
#         'crayfish': 'lentils',
#         'lobster': 'lentils',
#         'shrimp': 'lentils',
#         'prawns': 'lentils',
#         'oyster': 'lentils',
#         'mussel': 'lentils' ,
#         'clams': 'lentils'
#     },
#     'grill':{
#         'chicken': 'tofu',
#         'turkey': 'tofu',
#         'beef': 'mushroom',
#         'lamb': 'mushroom',
#         'pork': 'jackfruit',
#         'fish': 'tofu',
#         'ground': 'beans',
#         'ham': 'tempeh',
#         'liver': 'tofu',
#         'bacon': 'vegetarian bacon',
#         'sausage': 'tofu',
#         'veal': 'seitan',
#         'carp': 'lentils',
#         'catfish': 'lentils',
#         'salmon': 'lentils',
#         'tilapia': 'lentils',
#         'tuna': 'lentils'
#         'trout': 'lentils',
#         'crayfish': 'lentils',
#         'lobster': 'lentils',
#         'shrimp': 'lentils',
#         'prawns': 'lentils',
#         'oyster': 'lentils',
#         'mussel': 'lentils' ,
#         'clams': 'lentils'
#     },
#     'steam':{
#         'chicken': 'tofu',
#         'turkey': 'tofu',
#         'beef': 'mushroom',
#         'lamb': 'mushroom',
#         'pork': 'jackfruit',
#         'fish': 'tofu',
#         'ground': 'beans',
#         'ham': 'tofu',
#         'liver': 'tofu',
#         'bacon': 'vegetarian bacon',
#         'sausage': 'tofu',
#         'veal': 'seitan',
#         'carp': 'lentils',
#         'catfish': 'lentils',
#         'salmon': 'lentils',
#         'tilapia': 'lentils',
#         'tuna': 'lentils'
#         'trout': 'lentils',
#         'crayfish': 'lentils',
#         'lobster': 'lentils',
#         'shrimp': 'lentils',
#         'prawns': 'lentils',
#         'oyster': 'lentils',
#         'mussel': 'lentils' ,
#         'clams': 'lentils'
#     },
#     'sautee':{
#         'chicken': 'tofu',
#         'turkey': 'tofu',
#         'beef': 'mushroom',
#         'lamb': 'mushroom',
#         'pork': 'jackfruit',
#         'fish': 'tofu',
#         'ground': 'beans',
#         'ham': 'tempeh',
#         'liver': 'tofu',
#         'bacon': 'vegetarian bacon',
#         'sausage': 'tofu',
#         'veal': 'seitan',
#         'carp': 'lentils',
#         'catfish': 'lentils',
#         'salmon': 'lentils',
#         'tilapia': 'lentils',
#         'tuna': 'lentils'
#         'trout': 'lentils',
#         'crayfish': 'lentils',
#         'lobster': 'lentils',
#         'shrimp': 'lentils',
#         'prawns': 'lentils',
#         'oyster': 'lentils',
#         'mussel': 'lentils' ,
#         'clams': 'lentils'
#     }
# }
class Recipe(object):

    def __init__(self, recipe_dic):
        self.recipe_name = recipe_dic["name"]
        # list of ingredients objects
        ingredients_list = recipe_dic['ingredients']
        ingredient_objects = []
        for ing in ingredients_list:
            ingredient_objects.append(Ingredient(ing))
        self.ingredients = ingredient_objects
        # directions object
        self.directions = recipe_dic['directions']

    def to_healthy(self):
        # returns a copy of healthy version of recipe

        # make ingredients healthy
        healthy_ingredients = copy.deepcopy(self.ingredients)
        for ingredient in healthy_ingredients:
            ingredient = ingredient.to_healthy()


        # make directions healthy
        healthy_directions = copy.deepcopy(self.directions)

        for i in range(len(healthy_directions)):
            curr_direction = healthy_directions[i]
            #print(curr_direction)
            for unhealthy_ing in healthy_substitutes:
                if unhealthy_ing in curr_direction:
                    curr_direction = curr_direction.replace(unhealthy_ing, healthy_substitutes[unhealthy_ing])
                    healthy_directions[i] = curr_direction
                    #print(unhealthy_ing)
                    #print(healthy_substitutes[unhealthy_ing])

        healthy_recipe = copy.deepcopy(self)

        # create new recipe object
        healthy_recipe.ingredients = healthy_ingredients
        healthy_recipe.directions = healthy_directions

        return healthy_recipe


    def to_veg(self):
        # returns a copy of vegetarian version of recipe
        # get mapping of meat to substitute
        methods = ['boil', 'bake','simmer','roast','fry','deep fry','deep-fry','stiry fry','stir-fry','grill','steam','sautee']
        meats_to_cooking_method = self.map_meat_to_cooking_method(self.directions, methods)
        meats_to_subtitute = self.meat_to_substitute(meats_to_cooking_method)

        # make ingredients veg
        veg_ingredients = copy.deepcopy(self.ingredients)
        for ingredient in veg_ingredients:
            ingredient = ingredient.to_veg(meats_to_subtitute)

        # make direction veg
        veg_directions = copy.deepcopy(self.directions)
        for i in range(len(veg_directions)):
            direction = veg_directions[i]
            for meat, substitute in meats_to_subtitute.items():
                if meat in direction:
                    veg_directions[i] = direction.replace(meat, substitute)
                    # print(direction)
                if 'meat' in direction:
                    if 'ground meat' in direction:
                        veg_directions[i] = direction.replace('ground_meat', substitute)
                    else:
                        veg_directions[i] = direction.replace('meat', substitute)
                # else:
                #     if 'ground' in meat:
                #         veg_directions[i] = direction.replace(meat.split(' ')[1], substitute)

        # create new recipe object
        veg_recipe = copy.deepcopy(self)
        # veg_recipe.recipe_name = "Vegetarian "+ veg_recipe.recipe_name
        veg_recipe.ingredients = veg_ingredients
        veg_recipe.directions = veg_directions

        return veg_recipe

    def meat_to_substitute(self, meat_to_cooking_method):
        global COOKING_METHOD_TO_SUBSTITUTE
        output = {}
        for meat, method in meat_to_cooking_method.items():
            if meat.split(' ')[0] != 'ground':
                output[meat] = COOKING_METHOD_TO_SUBSTITUTE[method][meat]
            else:
                output[meat] = COOKING_METHOD_TO_SUBSTITUTE[method]['ground']
        return output

    def map_meat_to_cooking_method(self, directions, methods):
        '''
        returns dictionary of mapping and meat cooking method
        '''
        meat_list = [r'ground (chicken|turkey|beef|lamb|pork)', 'chicken', 'turkey', 'beef', 'lamb', 'pork', 'fish'] #TODO: potentially add types of shellfish
        output = {}

        meat_directions = {}
        exclude_list = []
        cur_meat = None
        # get directions with meats only
        for direction in directions:
            for meat in meat_list:
                if meat in exclude_list:
                    continue
                if cur_meat != None:
                    for method in methods:
                        if method in direction:
                            output[cur_meat] = method
                else:
                    found_meat = re.search(meat, direction)
                    if found_meat:
                        cur_meat = found_meat[0]
                        meat_directions[found_meat[0]] = direction
                        # prevent duplicates with ground meats
                        # print(found_meat)
                        # to_exclude = found_meat[0].split()[1]
                        # exclude_list.append(to_exclude)
        return output

    def to_cuisine(self, cuisine):
        for i in self.ingredients:
            print("name:", i.name, "// unit:",i.unit, "// quantity:",i.quantity, "// prep:", i.prep)

        return cuisine
