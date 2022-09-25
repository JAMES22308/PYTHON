import math
import pyttsx3 
jarvis = pyttsx3.init()
rate = -5000
jarvis.setProperty('rate', rate)
name = input("name: ")
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / (height/100)**2
print(f"You BMI  is {bmi}")
if bmi <= 18.4:
    print(f"underweight.{name}")
    print(name)
elif bmi <= 24.9:
    print(name)
    print(f"yiee healthy si {name}")
    jarvis.say(f"yiee healthy si {name}")
elif bmi <= 29.9:
    print(name)
    print(f"You are over weight. {name}")
elif bmi <= 34.9:
    print(name)
    print(f"You are severely over weight. {name}")
elif bmi <= 39.9:
    print(name)
    print(f"You are obese.{name}")
else:
    print(name)
    print(f" you're literally unhealthy, obese.{name}")
jarvis.runAndWait()
