import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
dfs_past = []
bfs_past = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

def dfs(v):
    dfs_past.append(v)
    print(v, end=' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and i not in dfs_past:
            dfs(i)
def bfs(v):
    queue = deque([v])
    bfs_past.append(v)
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in range(1, n+1):
            if graph[x][i] ==1 and i not in bfs_past:
                queue.append(i)
                bfs_past.append(i)
dfs(v)
print()
bfs(v)