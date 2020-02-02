def s22019():
    number = int(input())
    primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    my_string = ''
    for i in range(number):
        num =int(input())*2
        if num+1 in primes:
            index = primes.index(num+1)
        elif num+2 in primes:
            index = primes.index(num+2)
        elif num+3 in primes:
            index = primes.index(num+3)
        elif num+4 in primes:
            index = primes.index(num+4)
        elif num+5 in primes:
            index = primes.index(num+5)
        elif num+6 in primes:
            index = primes.index(num+6)
        elif num+7 in primes:
            index = primes.index(num+7)
        elif num+8 in primes:
            index = primes.index(num+8)
        elif num+9 in primes:
            index = primes.index(num+9)
        elif num+10 in primes:
            index = primes.index(num+10)
        
        for j in range(int(index)):
            my_sum = 0
            higher = primes[j]
            for k in range(int(index)):
                lower = primes[k]
                my_sum = higher + lower
                if my_sum == num:
                    my_other_string = str(str(higher)+' '+str(lower)+'\n')
                    my_string = my_string + my_other_string
                    break
            if my_sum == num:
                break
    print(my_string)

s22019()