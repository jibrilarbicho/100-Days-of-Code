print("Wlecome to the roolerCaster")
heigh=int(input("What is your height in cm ?"))
if heigh > 120:print("You can ried the rollerCaster")
else:print("you must grow taller to ride the roller")
height=float(input("Enter your height in meter:"))
weight=float(input("Enter your weight in kg:"))
bmi=round(weight/height**2)
if bmi>18.5:
    print(f"Your BMI is:{bmi},you are underweight")
elif bmi<25:
    print(f"your BMI is:{bmi}.you  are at normal weight")