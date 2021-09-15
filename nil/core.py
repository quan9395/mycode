import speech_recognition
import pyttsx3

import understand

# Initializing
ear = speech_recognition.Recognizer()
mouth = pyttsx3.init()
brain = ""

# Listening

while True:
	with speech_recognition.Microphone() as mic:
			print("Nil: I'm listening")
			audio = ear.listen(mic)
	try:
		you = ear.recognize_google(audio)
	except:
		you = ""
	print("You: " + you)

	# Understanding
	brain = understand.nil_understand(you)


	# Speaking
	mouth.say(brain)
	print("Nil: " + brain)
	mouth.runAndWait()

	#exit
	if brain == "exit":
		mouth.say("Good bye")
		mouth.runAndWait()
		break