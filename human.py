import pyttsx3
import os
pyttsx3.speak("hello and welcome to python world")
print("Hello")
while True:
	print("How can I help you ?   ", end=" ")
	p=input()
	if (("don't" in p) or ("donot" in p) or ("do not" in p) or (" not " in p) or (" no " in p)):
		print("okay")
	else:
		if (("run in p") or ("execute" in p) or("launch" in p) or ("open" in p)) and (("chrome" in p) or ("browser" in p)):
	     		os.system("chrome")
		elif (("run in p") or ("execute" in p) or("launch" in p) or ("open" in p)) and (("notepad" in p) or ("editor" in p)):
	     		os.system("notepad")
		elif (("run in p") or ("execute" in p) or("launch" in p) or ("open" in p)) and (("media player" in p) or ("music player" in p)):
	     		os.system("wmplayer")
		elif (("run in p") or ("execute" in p) or("launch" in p) or ("open" in p)) and (("control panel" in p) or ("control board" in p)):
	     		os.system("control panel")
		elif (("run in p") or ("execute" in p) or("launch" in p) or ("open" in p)) and ("youtube" in p):
	     		os.system("chrome  youtube.com")
		elif (("run in p") or ("execute" in p) or("launch" in p) or ("open" in p)) and  ("whatsapp" in p):
	     		os.system("chrome  web.whatsapp.com")
		elif (("run in p") or ("execute" in p) or("launch" in p) or("login" in p) or ("open" in p)) and  (("mail box" in p) or ("gmail box" in p)  or ("inbox" in p) or ("gmail inbox" in p) or ("gmail" in p) or ("mail" in p)):
	     		os.system("chrome  https://mail.google.com/mail/u/0/#inbox")
		elif (("run" in p) or ("execute" in p) or("launch" in p) or ("open" in p) or ("login" in p)) and ("yahoo" in p):
	     		os.system("chrome  yahoo.com")
		elif (("run" in p) or ("execute" in p) or("launch" in p) or ("open" in p) or ("login" in p)) and (("facebook" in p) or ("fb" in p)):
	     		os.system("chrome  facebook.com")
		elif (("go" in p) or ("exit" in p) or("quit" in p) or ("logout" in p) or ("offline" in p) or ("leave" in p) or ("depart" in p)):
	     		break
		else :
	     		print("It doesn't support")