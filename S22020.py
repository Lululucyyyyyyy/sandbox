rows = int(input())
columns = int(input())
positions = []
all_positions = []
last_position = [rows-1, columns-1]
found = False
string = 'no'

def s22020():
    my_arr = []
    factors = []
    for i in range(rows):
        row = input().split(' ')
        roww = []
        for num in row:
            roww.append(int(num))
        my_arr.append(roww)
    positions.append([0, 0])
    all_positions.append([0, 0])
    loop(positions, my_arr, found)
    print(string)

def factor(x):
    factors = []
    for i in range(1, x+1):
        if x % i == 0:
            factors.append(i)
    return factors

def loop(positions, arr, found):
    pos = positions[0]
    num = arr[pos[0]][pos[1]]
    factors = factor(num)
    for i in range(int(len(factors)/2)+1):
        length = len(factors) - 1
        if factors[i] <= columns and int(num/factors[i]) <= rows:
            poss = [int(num/factors[i]-1), int(factors[i]-1)]
            if poss not in all_positions:
                if poss == last_position:
                    found = True
                    print('yes')
                    exit()
                    break
                positions.append(poss)
                all_positions.append(poss)
        if int(num/factors[i]) <= columns and factors[i] <= rows:
            poss = [int(factors[i]-1), int(num/factors[i]-1)]
            if poss not in all_positions:
                if poss == last_position:
                    found = True
                    print('yes')
                    exit()
                    break
                positions.append(poss)
                all_positions.append(poss)
    if found == False:
        positions.remove(pos)
        if len(positions) != 0:
            loop(positions, arr, found)
s22020()