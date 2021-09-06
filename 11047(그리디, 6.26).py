array = []

n, k = map(int, input().split())

for _ in range(n):
    array.append(int(input()))

count = 0
comp = k
for num in reversed(array):
    while comp >= num:
        count += 1
        comp -= num
print(count)
