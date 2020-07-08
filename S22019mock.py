def i_luv_pusheen():
    num = int(input())
    my_list = []
    for i in range(num):
        my_list.append(input())
    x = 0
    startx = 0
    endx = 0
    first = False
    last = False
    for i in range(num):
        row = my_list[i].split(' ')
        for j in range(num):
            x += 1
            if int(row[j]) != x and first==False:
                startx = j
                first = True
            if first==True and int(row[j]) == x:
                endx = j
                last = True
                break
        if last:
            break
    if first == False:
        print(0)
    else: 
        if endx == 0:
            endx = num
        print(endx-startx)

    

i_luv_pusheen()