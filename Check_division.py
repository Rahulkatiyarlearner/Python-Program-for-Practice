num = int(input("Enter the number you got out of 300: "))
percentage = (num / 300) * 100
print("Your percentage is: ", percentage)
if num > 300:
    print("you have provided wrong marks")
elif percentage >= 60:
    print("you got the first division")
elif percentage >= 50 and percentage < 60:
    print("you got the second division")
elif percentage >= 33 and percentage < 50:
    print("you got the third division") 
else:
    print("you are fail")