import math


area = 0.0
side = 0
length = 0
width = 0
height = 0
base = 0
pi = math.pi
radius = 0
print("==================")
print("Area Calculator 📐")
print("==================")
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")
calculator = int(input("Which shape: "))
if calculator == 1:
    height = int(input("height: "))
    base = int(input("base: "))
    area = (height * base)/2
    print("The area is " + f"{area}")
elif calculator == 2:
    length = int(input("lenght: "))
    width = int(input("width: "))
    area = (length * width)
    print("The area is " + f"{area}")
elif calculator == 3:
    side = int(input("side: "))
    area = (side**2)
    print("The area is " + f"{area}")
elif calculator == 4:
    radius = int(input("radius: "))
    area = pi * (radius**2)
    print("The area is " + f"{area:.2f}")
elif calculator == 5:
    print("Quited successfully")
else:
    print("Invalid Request.")