import sys

coins = [500, 100, 50, 10, 5, 1]
change= 1000 - int(sys.stdin.readline())

count = 0
for coin in coins:
    while change >= coin:
        change -= coin
        count += 1

print(count)


    

