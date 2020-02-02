def s42019():
    num_places, num_per_day = input().split(' ')
    points = input().split(' ')
    days = num_places/num_per_day
    if days%1!=0:
        days = int(days)+1
    

s42019()