from datetime import date, datetime

def nil_understand(you):
	if you == "":
		brain = "I can't hear you, try again"
	elif you == "hello":
		brain = "good day"
	elif you == "bye":
		brain = "exit"
	elif "time" in you:
		now = datetime.now()
		brain = now.strftime("%H hours %M minutes %S seconds")
	elif "today" in you:
		today = date.today()
		brain = today.strftime("%B %d, %Y")
	else:
		brain = "..."
	return brain

