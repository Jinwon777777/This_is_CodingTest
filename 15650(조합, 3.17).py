from itertools import combinations

n, m = map(int, input().split())

item = []
for i in range(1, n + 1):
    item.append(str(i))

x = combinations(item, m)

for tis in x:
    print(' '.join(tis))
