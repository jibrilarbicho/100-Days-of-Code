height = float(input("'Enter your Height"))
weight = int(input("Enter your Weight"))
if height > 3:
    raise ValueError("The height is not graeter than 3m")
bmi = weight / height**2
print(bmi)
