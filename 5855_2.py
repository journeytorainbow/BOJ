import sys 

coins = [500, 100, 50, 10, 5, 1]
change = 1000 - int(sys.stdin.readline())

count = 0
for coin in coins:
    count += change//coin
    change %= coin

print(count)