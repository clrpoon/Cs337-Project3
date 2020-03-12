from rasa_interface import rasa_output

text = ""
while text != '/exit':
    text = input("Type here \n")
    res = rasa_output(text)
    print(res)