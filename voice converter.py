# import pyttsx3
# import time
# assistant = "jarvis"
# boss = "james"
# rate = -500
# friend = pyttsx3.init()
# friend.setProperty('rate', rate+50)
# friend.say(f"hello {boss} I'm {assistant} "+"nice to meet you")
# friend.runAndWait()

import random
import pyttsx3
assistant = "jarvis"
friend = pyttsx3.init()
member = ['james',"coline","molina"]
leader = random.choice(member)
friend.say(f"hello i'm {assistant} and i choose {leader} to be a leader tuck off")
print(f"hello i'm {assistant} and i choose {leader} to be a leader tuck off")
friend.runAndWait()