n = int(input("Enter limit"))

mob = 0
name = ""
for i in range(0,n):
    mob = int(input("Enter the mobile number "))
    name = input("Enter the name ")
    z2 = dict({mob:name})
    m.update(z2)

print(m)

n = int(input("Enter the mobile number to search "))
print("The name of the person is ", m[n])