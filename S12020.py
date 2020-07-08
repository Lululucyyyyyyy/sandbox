import sys
def s12020():
    num = int(input())
    dist = []
    time = []
    time2 = []
    maxv = 0
    for i in range(num):
        line = input()
        temp_list = line.split(' ')
        y = int(temp_list[0])
        x = int(temp_list[1])
        dist.append(x)
        time.append(y)
        time2.append(y)
    time.sort()
    dist2 = []
    for x in time:
        i = time2.index(x)
        dist2.append(dist[i])
        
    for i in range(num-1):
        distance = abs(dist2[i] - dist2[i+1])
        timee = abs(time[i] - time[i+1])
        speed = distance / timee
        if maxv < speed:
            maxv = speed
    print(maxv)

s12020()