n, m, r = map(int, input().split())

item = list(map(int, input().split()))
item.insert(0, 0)
INF = 1e9
graph = [[INF] * (n + 1) for _ in range(n + 1)]
result = []

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n + 1):
    count = item[i]
    for j in range(1, n + 1):
        if graph[i][j] <= m and graph[i][j] != 0:
            count += item[j]
    result.append(count)

print(max(result))
