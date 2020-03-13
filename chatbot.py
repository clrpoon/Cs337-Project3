from RecipeFetcher import *
from recipe import *
from nltk.corpus import wordnet as wn
import random 
from rasa_interface import rasa_output

# stores current recipe that the user is interacting with, current_recipe is None if no current recipe found 
global current_recipe 
# step index represents the step that the user is currently on, starts at step 1
global step_index
global rf 

current_recipe = None  
step_index = 1 
rf = RecipeFetcher()

if __name__ == "__main__":
    chatbot()

# Start the chatbot 
def chatbot(): 
    # initialize recipe fetcher object, can be used to scrap any food

    # GREETING 
    print('Hello, welcome to BBB. Please start typing to interact with our AllRecipes.com chatbot.')

    while True: 
        # take in user input 
        user_input = input('Type here \n')

        # use rasa to determine intent, and then process the json response 
        res = rasa_output(user_input)
        intent, confidence = process_intent(res)
    
        # act on whatever intent is determined by rasa
        act_on_intent(intent, confidence, user_input) 

def process_intent(intent_json): 
    try:
        intent = intent_json['intent']['name']
        confidence = intent_json['intent']['confidence']
    except:
        intent = ''
        confidence = -1 
    return intent, confidence 

def act_on_intent(intent, confidence, user_input):
    if confidence < 0.05:
        # if confidence below threshold, do not use that intent 
        print("Sorry, BBB does not understand that yet, please try another phrase") 

    elif intent == 'greeting':
        utter_greeting()

    elif intent == 'goodbye':
        # utter_goodbye
        pass

    elif intent == 'prompt_recipe_search':
        prompt_recipe_search()

    elif intent == 'prompt_recipe_search_for':
        prompt_recipe_search_for(user_input)  

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
    
    elif intent == 'thanks':
        # ask if should go on to next step 
        pass
    
    elif intent == 'find_new_recipe': 
        # reset recipe to -1 
        # prompt what you want user to cook again 
        pass


def utter_greeting():
    greetings = ['Hi, my name is BBB', 'Welcome to BBB', "Hello!", "Greetings.", "Howdy!"]
    print(random.choice(greetings))

def prompt_recipe_search():
    print("Sure thing! Please specify a URL from allrecipes or a type of food (e.g: steak, chicken lasagna, etc)")

# user input must be food or URL 
def prompt_recipe_search_for(user_input): 
    # only accepts food or URL 
    if 'allrecipes.com' in user_input.lower(): 
        for word in user_input.lower().split():
            if 'allrecipes.com' in word:
                cleaned_input = word 
        recipe_json = rf.scrape_recipe("", cleaned_input)
    else: 
        # search for the food item
        recipe_json = rf.find_recipe(user_input)

    try: 
        recipe = Recipe(recipe_json)
        # set current recipe 
        current_recipe = recipe
        print("Here is your recipe: \n")
        recipe.print_recipe() 
    except:
        # if invalid search query 
        print('Invalid search query, please try your search again.')