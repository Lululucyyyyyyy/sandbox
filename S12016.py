def ragaman():
    first = input()
    second = input()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    current_list = []
    wildcards = 0
    others = 0
    for letter in first:
        current_list.append(letter)
    for letter in second:
        if letter in current_list:
            current_list.remove(letter)
        elif letter == '*':
            wildcards += 1
    extras = len(current_list)
    if len(current_list) == 0 or extras == wildcards:
        print('A')
    else:
        print('N')
    
ragaman()