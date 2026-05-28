num = eval(input("Please provide the range: "))
first_num = 0
second_num = 1
for num in range(0,num):
    if num <= 1:
        Next_num = num
    else :
        Next_num = first_num + second_num
        first_num = second_num
        second_num = Next_num
    print(Next_num)

