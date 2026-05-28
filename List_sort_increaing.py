a =eval(input("Enter the limit"))
lst = []
for a in range(1,a+1):
    n = eval(input("Enter a element in list "))
    lst.append(n)
print("The list is ", lst)
l = len(lst)
for i in range(l):
    for j in range(0,l-i-1):
        if lst[j] > lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
            
print("The sorted list is ", lst)