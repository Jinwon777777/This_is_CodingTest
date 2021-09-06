from collections import deque

n, k = map(int, input().split())

q = deque()
ans = []

for num in range(1, n + 1):
    q.append(num)

count = 0
while q:
    if count == k-1:
        ans.append(str(q.popleft()))
        count = 0
    else:
        q.append(q.popleft())
        count += 1

print("<" + ", ".join(ans)+">")
