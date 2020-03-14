# CS 337 (NLP) Project2: Recipes

INSTRUCTIONS TO RUN THIS PROJECT: 
1. 'pip install -r requirements.txt' 
2. run 'python3 chatbot.py'
3. have fun ! 

About:
We used Rasa to define intents, and keep context of what recipe you are using and what step you are on. We process all intents differently, for example: 
1. showing ingredients or directions (only if you've searched a recipe)
2. navigating to the proper step when you ask for a certain step 
3. returning youtube links for "how to" questions
4. return dictionary links for "what is" questions 
(and more)
5. clearing the recipe and asking if you want to cook something else if you say you don't want to cook this anymore
6. greeting you with hellos and goodbyes

~ Thanks for a great quarter! ~
