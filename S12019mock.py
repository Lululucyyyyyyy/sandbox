from decimal import Decimal

def my_function():
    num = int(input())
    total = 0
    for i in range(num):
        total += int(input())
    av = total / num
    print(av)

my_function()