def s12019():
    my_input = input()

    v = my_input.count('V')
    h = my_input.count('H')

    my_list = [[1, 2], 
                [3, 4]]

    if v%2==0:
        pass
    else:
        my_list[0][1]=1
        my_list[0][0]=2
        my_list[1][1]=3
        my_list[1][0]=4
    if h%2==0:
        pass
    else:
        temp = my_list[0][0]
        my_list[0][0]=my_list[1][0]
        my_list[1][0]= temp
        temp = my_list[0][1]
        my_list[0][1]=my_list[1][1]
        my_list[1][1]=temp
    print(str(my_list[0][0])+' '+str(my_list[0][1]) +'\n'+ str(my_list[1][0])+' '+str(my_list[1][1]))
s12019()