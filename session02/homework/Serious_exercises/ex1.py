print("Nice to meet you!")
mass= float(input("How much do you weigh?"))
print("Your's mass:", mass, "kg")
height=int(input("Your's height?"))/100
print("Your's heigt:", height, "m")
BMI = mass/height**2
print("Your's BMI", BMI)

if BMI < 16:
    print("Severely underweight")
elif BMI <= 18.5:
    print("Underweight")
else:
    if BMI <= 25:
        print("Normal")
    elif BMI <= 30:
        print("Overweight")
    else:
        print("Obese")
