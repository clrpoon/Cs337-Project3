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

# Start the chatbot 
def chatbot(): 
    # initialize recipe fetcher object, can be used to scrap any food

    # GREETING 
    print('Hello, welcome to BBB. Please start typing to interact with our AllRecipes.com chatbot.')

    while True: 
        # take in user input 
        print('\n')
        user_input = input('Type here... \n')

        # use rasa to determine intent, and then process the json response 
        res = rasa_output(user_input)
        # print(res)
        intent, confidence = process_intent(res)
    
        # act on whatever intent is determined by rasa
        act_on_intent(intent, confidence, user_input) 

def process_intent(intent_json): 
    try:
        # print(intent_json)
        intent = intent_json['intent']['name']
        confidence = intent_json['intent']['confidence']
    except:
        # print('failed')
        intent = ''
        confidence = -1 
    return intent, confidence 

def act_on_intent(intent, confidence, user_input):
    # print('----------------------')
    # print(intent)
    # print(confidence)
    # print('----------------------')
    if confidence < 0.05:
        # if confidence below threshold, do not use that intent 
        print("Sorry, we're not completely sure what you mean. Please try again") 

    elif intent == 'greet':
        utter_greeting()

    elif intent == 'goodbye':
        utter_goodbye() 
        pass

    elif intent == 'prompt_recipe_search':
        prompt_recipe_search()

    elif intent == 'prompt_recipe_search_for':
        prompt_recipe_search_for(user_input)  

    elif intent == 'how_to':
        # look up how to on youtube or somwhere
        how_to(user_input)

    elif intent == 'look_up': 
        # look up definition
        look_up(user_input)

    elif intent == 'show_directions': 
        # show all directions
        # if recipe is None, prompt user to search for a food 
        show_directions()

    elif intent == 'show_ingredients': 
        # show ingredients 
        # if recipe is None, prompt user to search for a food 
        show_ingredients

    elif intent == 'navigate_directions':
        # show navigation 
        # if recipe == -1, propmt user to search for a food 
        navigate_directions(user_input) 
    
    elif intent == 'thanks':
        # ask if should go on to next step 
        utter_thanks()
    
    elif intent == 'find_new_recipe': 
        # reset recipe to -1 
        # prompt what you want user to cook again 
        find_new_recipe() 

    else: 
        print("Sorry, BBB does not understand that yet, please try another phrase") 


def utter_greeting():
    greetings = ['Hi, my name is BBB', 'Welcome to BBB', "Hello!", "Greetings.", "Howdy!"]
    print(random.choice(greetings))

def utter_goodbye():
    goodbyes = ['Thanks and come again!', 'Goodbye!', "See ya later", "Bye!", "Have a nice day!"]
    current_recipe = None 
    step_index = 1
    print(random.choice(goodbyes))

def prompt_recipe_search():
    print("Sure thing! Please specify a URL from allrecipes or a type of food (e.g: steak, chicken lasagna, etc)")

# user input must be food or URL ---------------------------------------------------EITHER MODIFY THIS TO PARSE THE FOOD NAME OUT OF THE STRING OR MODIFY THE INTENTS
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

def how_to(user_input):
    print('We found this video showing you', user_input,'\n')
    # RETURN YOUTUBE LINK RESULT HERE ---------------------------

def look_up(user_input):
    print('We found this meaning for what you were wondering about:\n')
    # RETURN DICTIONARY LOOKUP RESULT HERE ---------------------------

def show_directions(): 
    # make sure this if condition works, I don't use "is None" very often  
    if current_recipe is None: 
        prompt_food = -1 
        while prompt_food not in [0, 1]: 
            prompt_food = input('You are not currently looking at a recipe, would you like to search for one? [0] for NO, [1] for YES.')
            if(prompt_food == 0):
                print("Ok, sounds good!")
            elif(prompt_food == 1):
                prompt_recipe_search()
            else:
                print("Sorry, invalid input. Please try again.")
    else: 
        print("Here are the directions to your recipe:\n")
        current_recipe.print_directions() 

def show_ingredients(): 
    if current_recipe is None: 
        prompt_food = -1 
        while prompt_food not in [0, 1]: 
            prompt_food = input('You are not currently looking at a recipe, would you like to search for one? [0] for NO, [1] for YES.')
            if(prompt_food == 0):
                print("Ok, sounds good!")
            elif(prompt_food == 1):
                prompt_recipe_search()
            else:
                print("Sorry, invalid input. Please try again.")
    else: 
        print("Here are the ingredients for your recipe:\n")
        current_recipe.print_ingredients() 

def navigate_directions(user_input): 
    # BASED ON THE CURRENT STEP, FIGURE OUT AND NAVIGATE TO THAT STEP 
    pass 

def find_new_recipe(): 
    print("Ok, we'll find you a different recipe")
    print("Please specify a URL from allrecipes or a type of food (e.g: steak, chicken lasagna, etc)")
    current_recipe = None
    step_index = 1 

if __name__ == "__main__":
    chatbot()