x = int(input("Please provide a number: "))
p = int(input("Please provide the power: "))
y = x
for i in range(1,p):
    y = y * x
print(y)