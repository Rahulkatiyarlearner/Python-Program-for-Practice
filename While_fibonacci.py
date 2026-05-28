a = eval(input("Please provide the range: "))
i = 0
first_num = 0
second_num = 1
while i < a :
    if i <= 1 :
        Next_num = i
    else :
        Next_num = first_num + second_num
        first_num = second_num
        second_num = Next_num
    print(Next_num)
    i += 1
