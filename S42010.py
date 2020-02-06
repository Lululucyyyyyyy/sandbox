def s42010():
    num = int(input())
    corner = [ 0 for i in range(999) ]
    cost = [ 0 for i in range(999) ]
    #initialize graph
    graph = [ [ 999 for i in range(num) ] for j in range(num) ]
    for j in range(num):
        graph[j][j]=0

    #initialize input grid
    my_input = [ [ Info() for i in range(1001) ] for j in range(1001) ]

    #input section
    for i in range(num):
        my_list = input().split(' ')
        num_edges = int(my_list[0])
        for k in range (num_edges):
            corner[k] = int(my_list[k+1])
        for k in range(num_edges):
            cost[k] = int(my_list[k+1+num_edges])
        
        for k in range(num_edges):
            j = (k+1)%num_edges
            
            if my_input[corner[k]][corner[j]].cost > 0:
                if graph[i][my_input[corner[k]][corner[j]].animal]>cost[k]:
                    graph[i][my_input[corner[k]][corner[j]].animal] = cost[k]
                    graph[my_input[corner[k]][corner[j]].animal][i] = cost[k]

                my_input[corner[k]][corner[j]].animal = -1
                my_input[corner[j]][corner[k]].animal = -1
            
            else:
                my_input[corner[k]][corner[j]].cost = cost[k]
                my_input[corner[k]][corner[j]].animal = i
                my_input[corner[j]][corner[k]].cost = cost[k]
                my_input[corner[j]][corner[k]].animal = i
    for i in range(1001):
        for j in range(1001):
            print(num)
            print(graph[my_input[i][j].animal])
            print(graph[my_input[i][j].animal][num])
            print(my_input[i][j].cost)
            if my_input[i][j].animal >= 0:
                if graph[my_input[i][j].animal][num] > my_input[i][j].cost:
                    graph[my_input[i][j].animal][num] = my_input[i][j].cost
                    graph[n][my_input[i][j].animal] = my_input[i][j].cost
    answer1 = prims(num)
    answer2 = primes(num+1)
    print(min(answer1, answer2))

class Info():
    animal = -1
    cost = 0
    def Info(a, c):
        animal = a
        cost = c

def prims(n):
    unseen = 999999
    val = [ [-unseen for i in range(n+1)] for k in range(n)]
    val[0] = -(unseen + 1)
    min = 1
    while True:
        k = min
        val [k] = -val [k]
        min = 0
        if val[k] == unseen:
            val[k] = 0
        for t in range(n):
            if vak[t] < 0:
                if graph[k-1][t-1] != 999 and val[t] < -(grapg[k-1][t-1]):
                    val[t] = -(graph[k-1][t-1])
                if val[t] > val[min]:
                    min = t
        if min == 0:
            break
    answer = 0
    for i in range(n+1):
        answer += val[i]
    return answer

s42010()