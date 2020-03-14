from rasa.cli.utils import print_success
from rasa.nlu.model import Interpreter
from rasa.nlu.utils import json_to_string


# path of your model
rasa_model_path = "bbb/models/model4/nlu"

# create an interpreter object
interpreter = Interpreter.load(rasa_model_path)

def rasa_output(text):
    message = str(text).strip()
    result = interpreter.parse(message)
    return result
