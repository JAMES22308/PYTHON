import math
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height/100)**2

print(f"You BMI  is {bmi}")

if bmi <= 18.4:
    print("underweight.")
elif bmi <= 24.9:
    print("Yieee hilti🤣.")
elif bmi <= 29.9:
    print("You are over weight.")
elif bmi <= 34.9:
    print("You are severely over weight.")
elif bmi <= 39.9:
    print("You are obese.")
else:
    print(" you're literally unhealthy, obese.")