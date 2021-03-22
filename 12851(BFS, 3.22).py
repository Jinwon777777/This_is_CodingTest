from collections import deque

x, y = map(int, input().split())

check = [0] * (100001)

q = deque()
q.append((0, x))
count = 0
t = -1
while q:
    s, num = q.popleft()
    check[num] = 1
    if t != -1 and s == t + 1:
        break
    if num == y:
        count += 1
        t = s
    else:
        if (num - 1) >= 0 and (num - 1) <= 100000 and check[num - 1] == 0:
            q.append((s + 1, num - 1))
        if (num + 1) >= 0 and (num + 1) <= 100000 and check[num + 1] == 0:
            q.append((s + 1, num + 1))
        if (num * 2) >= 0 and (num * 2) <= 100000 and check[num * 2] == 0:
            q.append((s + 1, num * 2))

print(t)
print(count)
