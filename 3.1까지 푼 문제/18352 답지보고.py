import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

path = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    path[a].append(b)

distance = [-1]*(n+1)

distance[x] = 0

q = deque([x])

while q:
    node = q.popleft()
    for p in path[node]:
        if distance[p] == -1:
            distance[p] = distance[node] + 1
            q.append(p)

check = False
ans = []
for j in range(len(distance)):
    if distance[j] == k:
       ans.append(j)
       check = True

if check == False:
    print(-1)
else:
    for com in ans:
        print(com)