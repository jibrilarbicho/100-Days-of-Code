import math

def paint_calc(height,width,cover):
    area=height*width
    num_of_cans=math.ceil(area/cover)
    print(f"you wi'll new to buy {num_of_cans}  cans of paint")
height=float(input("Enter the height"))    
width=float(input("Enter the width"))    
cover=float(input("Enter number fo the cover"))
paint_calc(height,width,cover)    
