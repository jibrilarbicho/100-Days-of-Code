print("123"+"456")
print(123+456)
numChar=len("welcome to jimma abba jifar")
print(type(numChar))
name=len("Kebede Zeleke")
#converting number into integer
numchar=str(name)
print("Your name has " +numchar +" Characters")
print(100 +float("100.73"))
print(str(100)+str(100))
print("hello"[3])
# Number manipulation and F string
print(int(8/3))
print(round(8/3,3))
# f String 
score=10
height=176
wining=True
print(f"your score is {score},your height is {height}, You are winning is {wining}")
age=input("Enter you age")
age_as_int=int(age)
years_reamaining=90-age_as_int
days_remaining=years_reamaining*365
weeks_remaining=years_reamaining*52
months_remainig=years_reamaining*12
print(f"you have {days_remaining} days,{weeks_remaining} weeks,{months_remainig} months left")
# Tip Calculator
print("Wlecome to tip calcultor")
total_bill = float(input("What was the total bill $"))
tip_percentage = int(input("How much would you like to give as a tip? 10, 12, or 15"))
people = int(input("How many people to split the bill?"))
tip_amount = total_bill * (tip_percentage / 100)
bill_with_tip = total_bill + tip_amount

amount_per_person = bill_with_tip / people
final_amount = round(amount_per_person, 2)

print(f"Each person should pay ${final_amount:.2f}")
