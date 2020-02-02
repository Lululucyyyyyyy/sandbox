def s32019():
    my_list = []
    my_list.append(input().split())
    my_list.append(input().split())
    my_list.append(input().split())
    num = 0
    my_string = ""

    for i in range(3):
        num = num + (my_list[i]).count('X')

    if num <=2:
        for i in range(3):
            row = my_list[i]
            if 'X' in row:
                index = row.index('X')
                if index==1:
                    d = (int(row[2]) - int(row[0]))/2
                    row[index] = int(row[0])+d
                elif index==0:
                    d = (int(row[2]) - int(row[1]))
                    row[index] = row[1]-d
                else:
                    d = row[1]-row[0]
                    row[index] = row[2]-d
            #for j in range(3):s
                #my_string += int(my_list[i][j])
                #my_string += ' '
            print(int(a) for a in my_list[i])
            #print(int(my_list[i][0]) + ' ' +  int(my_list[i][1]) + ' '+ int(my_list[i][2]))
            #my_string += '\n'
    else:    
        dx1 = 0
        dy1 = 0
        dx2 = 0
        dy2 = 0
        dx3 = 0
        dy3 = 0
        num1 = 0 
        num2 = 0 
        num3 = 0
        count = 0
        x1 = 0 
        x2 = 0 
        x3 = 0 
        y1 = 0 
        y2 = 0 
        y3 = 0
        yes1 = True
        yes2 = True
        yes3 = True
        for y in range(3):
            for x in range(3):
                var = my_list[y][x]
                if yes1 or yes2 or yes3:
                    if var != 'X':
                        count += 1
                        if count == 1:
                            num1= int(var)
                            x1=x
                            y1=y
                            yes1 = False
                        elif count ==2:
                            num2= int(var)
                            x2=x
                            y2=y
                            yes2 = False
                        else:
                            num3= int(var)
                            x3=x
                            y3=y
                            yes3 = False
                else:
                    break
        print(x1, x2, x3, y1, y2, y3, num1, num2, num3)
        dy = ((x2-x1)(num1 - num2) - (x1-x3)(num1-num2))/((x1-x3)(y2-y1)-(x2-x1)(y3-y1))
        dx= (num2 - num3 + dy*(y3-y2))/(x2-x3)
        base = num1 - x1*dx - y1*dy
        for y in range(3):
            for x in range(3):
                var = my_list[y][x]
                if var == 'X':
                    my_list[y][x] = base + x*dx + y*dy
                    my_string += str(my_list[y][x])
    #print(my_string)
                    

    '''
    num1 - x1*dx + x2*dx = num2 - y2*dy + y1*dy
    num1 - x1*dx + x3*dx = num3 - y3*dy + y1*dy
    num2 - x2*dX + x3*dx = num3 - y3*dy + y2*dy
    num1 - dx*(x2-x1) = num2 - dy*(y2-y1)
    num1 - dx*(x1-x3) = num2 - dy*(y3-y1)
    num2 - dx*(x2-x3) = num3 - dy*(y3-y2)
    dx= (num1 - num2 + dy*(y2-y1))/(x2-x1)
    dx= (num1 - num2 + dy*(y3-y1))/(x1-x3)
    dx= (num2 - num3 + dy*(y3-y2))/(x2-x3)
    (x1-x3)(num1 - num2 + dy*(y2-y1)) = (x2-x1)(num1 - num2 + dy*(y3-y1))
    (x1-x3)(dy*(y2-y1)) + (x1-x3)(num1-num2) = (x2-x1)(dy*(y3-y1)) + (x2-x1)(num1 - num2)
    (x1-x3)(dy*(y2-y1)) - (x2-x1)(dy*(y3-y1)) = (x2-x1)(num1 - num2) - (x1-x3)(num1-num2)
    dy = ((x2-x1)(num1 - num2) - (x1-x3)(num1-num2))/((x1-x3)(y2-y1)-(x2-x1)(y3-y1))
    dx= (num2 - num3 + dy*(y3-y2))/(x2-x3)
    '''
print(s32019())