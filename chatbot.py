from RecipeFetcher import *
from recipe import *
from nltk.corpus import wordnet as wn
import random 
from rasa_interface import rasa_output
from youtube_search import YoutubeSearch
from googlesearch import search 
import json

# stores current recipe that the user is interacting with, current_recipe is None if no current recipe found 
# global current_recipe 
# step index represents the step that the user is currently on, starts at step 1
# global step_index
# global rf 

current_recipe = -1  
step_index = 1 
rf = RecipeFetcher()

# Start the chatbot 
def chatbot(): 
    # initialize recipe fetcher object, can be used to scrap any food

    # GREETING 
    print('-------------------------------')
    print('Hello, welcome to BBB. Please start typing to interact with our AllRecipes.com chatbot.')

    while True: 
        # take in user input 
        # print('\n')
        user_input = input('Type here... \n')
        print('-------------------------------')
        # use rasa to determine intent, and then process the json response 
        res = rasa_output(user_input)
        print('BBB: -------------------------------')
        # print(res)
        intent, confidence = process_intent(res)
        # act on whatever intent is determined by rasa
        act_on_intent(intent, confidence, user_input) 
        print('-------------------------------')

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
        print("Sorry, we're not completely sure what you mean. Please try again.") 

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

    elif intent == 'what_is': 
        # look up definition
        what_is(user_input)

    elif intent == 'show_directions': 
        # show all directions
        # if recipe is None, prompt user to search for a food 
        show_directions()

    elif intent == 'show_ingredients': 
        # show ingredients 
        # if recipe is None, prompt user to search for a food 
        show_ingredients()

    elif intent == 'navigate_directions':
        # show navigation 
        # if recipe == -1, propmt user to search for a food 
        navigate_directions(user_input) 
    
    elif intent == 'thanks':
        # ask if should go on to next step 
        # utter_thanks()
        do = 'something'
    
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
    global step_index
    global current_recipe
    goodbyes = ['Thanks and come again!', 'Goodbye!', "See ya later", "Bye!", "Have a nice day!"]
    current_recipe = -1 
    step_index = 1
    print(random.choice(goodbyes))

def prompt_recipe_search():
    user_input = input("Sure thing! Please specify a URL from allrecipes.com or a type of food (e.g: steak, chicken lasagna, etc) \n")
    prompt_recipe_search_for(user_input)

# user input must be food or URL ---------------------------------------------------EITHER MODIFY THIS TO PARSE THE FOOD NAME OUT OF THE STRING OR MODIFY THE INTENTS
def prompt_recipe_search_for(user_input): 
    global step_index
    global current_recipe
    # only accepts food or URL 
    if 'allrecipes.com' in user_input.lower(): 
        for word in user_input.lower().split():
            if 'allrecipes.com' in word:
                cleaned_input = word 
        recipe_json = rf.scrape_recipe("", cleaned_input)
    else: 
        # search for the food item
        recipe_json = rf.find_recipe(user_input)
        # print(recipe_json, '---------------------------')

    # try: 
    recipe = Recipe(recipe_json)
    # set current recipe 
    current_recipe = recipe
    print("We found this recipe for you: \n")
    recipe.print_recipe_info() 
    # except:
    #     # if invalid search query
    #     print('Invalid search query, please try your search again.')

def how_to(user_input):
    print('We found this video showing you:', user_input,'\n')
    video_info = json.loads(YoutubeSearch(user_input, max_results=1).to_json())
    video_info = video_info["videos"][0]
    link = "youtube.com" + video_info["link"]
    print(link)
    # RETURN YOUTUBE LINK RESULT HERE ---------------------------

def what_is(user_input):
    print('We found this meaning for what you were wondering about:\n')
    found = False 
    for link in search(user_input, tld="co.in", num=15, stop=15, pause=2):
        if('dictionary' in link or 'merriam-webster' in link):
            print(link)
            found = True 
            break 
    if not found: 
        print("Could not find a good meaning for this phrase.")
    # RETURN DICTIONARY LOOKUP RESULT HERE ---------------------------

def show_directions(): 
    global step_index
    global current_recipe
    # make sure this if condition works, I don't use "is None" very often
    print(current_recipe)  
    if current_recipe == -1: 
        prompt_food = -1 
        while prompt_food not in ["0", "1"]: 
            prompt_food = input('You are not currently looking at a recipe, would you like to search for one? [0] for NO, [1] for YES.')
            if(prompt_food == "0"):
                print("Ok, sounds good!")
            elif(prompt_food == "1"):
                prompt_recipe_search()
            else:
                print("Sorry, invalid input. Please try again.")
    else: 
        print("Here are the directions to your recipe:\n")
        current_recipe.print_directions() 

def show_ingredients(): 
    global step_index
    global current_recipe

    if current_recipe == -1: 
        prompt_food = -1 
        print(prompt_food)
        while prompt_food not in ["0", "1"]: 
            prompt_food = input('You are not currently looking at a recipe, would you like to search for one? [0] for NO, [1] for YES.')
            if(prompt_food == "0"):
                print("Ok, sounds good!")
            elif(prompt_food == "1"):
                prompt_recipe_search()
            else:
                print("Sorry, invalid input. Please try again.")
    else: 
        print("Here are the ingredients for your recipe:\n")
        current_recipe.print_ingredients() 

def navigate_directions(user_input): 
    global step_index
    global current_recipe

    if current_recipe == -1: 
        prompt_food = -1 
        while prompt_food not in ["0", "1"]: 
            prompt_food = input('You are not currently looking at a recipe, would you like to search for one? [0] for NO, [1] for YES.')
            if(prompt_food == "0"):
                print("Ok, sounds good!")
            elif(prompt_food == "1"):
                prompt_recipe_search()
            else:
                print("Sorry, invalid input. Please try again.")
    else: 
        if 'next' in user_input:
            step_index += 1 
        elif 'back' in user_input:
            step_index -= 1 
        elif len([int(s) for s in user_input.split() if s.isdigit()]) > 0:
            step_index = [int(s) for s in user_input.split() if s.isdigit()][0]

        current_recipe.print_step(step_index)

def find_new_recipe(): 
    global current_recipe
    global step_index
    user_input = input("Ok, we'll find you a different recipe. Please specify a URL from allrecipes or a type of food (e.g: steak, chicken lasagna, etc) \n")
    prompt_recipe_search_for(user_input)
    # current_recipe = -1
    # step_index = 1 

if __name__ == "__main__":
    chatbot()