from RecipeFetcher import *
from recipe import *
from nltk.corpus import wordnet as wn
import random 

def main(): 
    # initialize recipe fetcher object, can be used to scrap any food
    rf = RecipeFetcher()
    # GREETING 
    print('Hello, welcome to BBB.')


    

    while True: 


        # prompt user for what recipe they want to find 
        food_name = input("Please enter what recipe you want to search for:\n")

        # fetch the allrecipes page
        recipe_json = rf.find_recipe(food_name)
        recipe = Recipe(recipe_json)
        # print initial recipe
        print("Here is the top result for your search: \n")
        recipe.print_recipe()

        # ask user what transformation they want to perform
        transformation = input("Please enter the transformation you want (vegetarian, healthy, asian). If none, enter any character:\n")
        if transformation == "vegetarian":
            veg = recipe.to_veg()
            veg.print_recipe()
        elif transformation == "healthy":
            healthy = recipe.to_healthy()
            healthy.print_recipe()
        elif transformation == "asian": 
            cuisine = input("Please input which asian region you want to transform your recipe to (current supported options include: chinese, korean, and thai):\n")
            while cuisine not in ["chinese", "korean", "thai"]:
                cuisine = input("Please input a supported option (chinese, korean, and thai):\n")
            asian = recipe.to_asian_cuisine(cuisine)
            asian.print_recipe()
        else: 
            print("Happy cooking!")

if __name__ == "__main__":
    main() 



global recipe
recipe = None 

def process_intent(intent_json): 
    try:
        intent = intent_json['intent']['name']
        confidence = intent_json['intent']['confidence']
    except:
        intent = ''
        confidence = -1 
    return intent, confidence 

def act_on_intent(intent, confidence):
    if intent == 'greeting':
        self.utter_greeting()
    elif intent == 'goodbye':
        # utter_goodbye
        pass
    elif intent == 'prompt_recipe_search':
        # utter please enter url or type name of food 
        # run ask the user what he wants to cook
        pass
    elif intent == 'prompt_recipe_search_for':
        self.prompt_recipe_search_for()  
    elif intent == 'how_to':
        # look up how to on youtube or somwhere
        pass
    elif intent == 'look_up': 
        # look up definition
        pass
    elif intent == 'show_directions': 
        # show all directions
        # if recipe == -1, propmt user to search for a food 
        pass
    elif intent == 'show_ingredients': 
        # show ingredients 
        # if recipe == -1, propmt user to search for a food 
        pass
    elif intent == 'navigate_directions':
        # show navigation 
        # if recipe == -1, propmt user to search for a food 
        pass
    elif intent == 'find_new_recipe': 
        # reset recipe to -1 
        # prompt what you want user to cook again 
        pass


def utter_greeting(self):
    greetings = ['hi, my name is BBB', 'welcome to BBB']
    print(random.choice(greetings))

def prompt_recipe_search_for(self, user_input): 
    # only accepts food or URL 
    if 'allrecipes.com' in user_input.lower(): 
        # search by url 
        pass
    else: 
        # search for the food item 
        pass 
