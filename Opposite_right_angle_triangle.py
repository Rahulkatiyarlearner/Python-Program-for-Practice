num = int(input("Enter the number of rows: "))
for i in range(num,0,-1):
    for j in range(0,i):
#print("*") normally moves to the next line.
#end="" prevents line change.
        print("*",end="") 
#print() moves the cursor to the next line  
    print()