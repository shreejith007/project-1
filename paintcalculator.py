import math
def paint_calculator(height,width,coverage):
    area =height*width
    no_can=math.ceil(area/coverage)
    print(f"you will need {no_can}  cans to paint")
print("-----------------------------------------------------------")
print("PAINT CALCULATOR")
print("-----------------------------------------------------------")
th=float(input("Enter the height"))
tw =float(input("Enter the width"))
cover=int(input("Enter the area of coverage"))

paint_calculator(height=th,width=tw,coverage=cover)
print("-----------------------------------------------------------")