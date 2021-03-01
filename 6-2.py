n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for com in array:
    print(com, end=' ')