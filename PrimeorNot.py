num = int(input("Enter a number "))   
limit = int(num/2)+1
for i in range(2, limit):
    remainder = num % i
    if remainder == 0:
        print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")