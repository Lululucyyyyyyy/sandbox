from itertools import permutations

def s32020():
    needle = input()
    haystack = input()
    counter = 0
    for p in set(permutations(needle)):
        p = ''.join(p)
        if p in haystack:
            counter += 1
    print(counter)

s32020()