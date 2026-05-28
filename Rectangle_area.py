def rectangle_area(l, b):
    area = l * b
    return area

password = str(input("Enter the password"))

if password == "11223344":
    print("password correct")
else:
    print("password incorrect")

length = float(input("Enter the length of the rectangle"))
breadth = float(input("Enter the breadth of the rectangle"))
print("The area of the rectangle is", rectangle_area(length, breadth))



