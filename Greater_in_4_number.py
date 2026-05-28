a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

if a > b and a > c and a > d:
    print("The greatest number is:", a)
elif b > c and b > d:
    print("The greatest number is:", b)
elif c > d:
    print("The greatest number is:", c)
elif d > c:
    print("The greatest number is:", d)
else:   
    print("All the four values are equal.")