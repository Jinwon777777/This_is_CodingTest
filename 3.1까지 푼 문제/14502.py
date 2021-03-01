n, m = map(int, input().split())

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
temp = [[0]*m for _ in range(n)]
result = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

def spread(x, y):
    for i in range(4):
        hx = x+dx[i]
        hy = y+dy[i]
        if 0 <= hx and hx < n and 0<=hy and hy < m:
            if temp[hx][hy] == 0:
                temp[hx][hy] = 2
                spread(hx, hy)

def get_zero():
    zero = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                zero += 1
    return zero

def dfs(count):
    global result
    ### 벽 3개 세우면 temp와 동기화
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    spread(i, j)
        ### 0의 갯수
        result = max(get_zero(), result)
        return
    ### 벽 세우기 이거 잘 이해하기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)