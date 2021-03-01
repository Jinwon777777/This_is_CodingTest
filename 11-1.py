n = int(input())

a = list(map(int, input().split()))
count = 0
while a:
    m = a.pop(a.index(max(a)))
    if len(a) >= m-1:
        for _ in range(m-1):
            a.pop(a.index(min(a)))
        count += 1
    else:
        count += 1
        break

print(count)