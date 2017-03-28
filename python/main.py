# Main file

from naoqi import ALProxy

# Modifier l'adresse IP et/ou le port en fonction du robot
tts = ALProxy("ALTextToSpeech", "127.0.0.1", 34120)
tts.say("Hello battleship")
