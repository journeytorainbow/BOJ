from collections import defaultdict
test = defaultdict(list)

test[1].append(3)
test[1].append(2)

print(test)

for i in test:
    i.sort()

print(test)