def cuboid_area(l,b,h):
    return 2 * (l*b + b*h + h*l)

lenght = float(input("Enter the lenght of the cuboid: "))
print("Thanks for providing the length")
breadth = float(input("Enter the breadth of the cuboid: "))
print("Thanks for providing the breadth")   
height = float(input("Enter the height of the cuboid: "))
print("Thanks for providing the height")
print("The surface area of the cuboid is", cuboid_area(lenght, breadth, height))