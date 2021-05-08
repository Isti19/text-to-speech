import os.path
import pyttsx3

engine = pyttsx3.init()

file = open("text.txt", "r")
# print(file.read())

engine.say(file.read())
engine.runAndWait()

