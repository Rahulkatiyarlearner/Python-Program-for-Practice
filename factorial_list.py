a = []
fact = []
ch = "y"

while ch == "y" or ch == "Y":
    n = int(input("Enter a element in list "))
    a.append(n)
    ch = input("Do you want to enter more element (y/n) ")

print("The list is ", a)

for i in a:
    f = 1
    for j in range(1, i + 1):
        f = f * j
    fact.append(f)

print("The factorial of the list is ", fact)