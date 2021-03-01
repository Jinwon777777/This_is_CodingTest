n = int(input())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

def dfs(x):
    result.append(x)
    for i in range(1, n+1):
        if (i not in result) and (graph[x][i] ==1):
            dfs(i)

    return len(result)-1

print(dfs(1))