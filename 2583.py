import sys
sys.setrecursionlimit(10000)

n, m, k = map(int, input().split())

graph = [[0]*(n) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

### 개수, 넓이 저장 리스트
count = 0
dimension = []

### graph에 벽을 표시
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

### DFS 만들기
def dfs(x, y):
    global count
    count+=1
    graph[x][y] = 1
    for t in range(4):
        hx = x+dx[t]
        hy = y+dy[t]
        if 0<=hx<m and 0<=hy<n and graph[hx][hy] == 0:
            dfs(hx, hy)
'''
def dfsj(x,y):
    global count
    if x<=-1 or x>=m or y<=-1 or y>=n:
        return False
    if graph[x][y] == 0:
        count += 1
        graph[x][y] = 2
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False
'''
for i in range(0, m):
    for j in range(0, n):
        if graph[i][j]==0: ### 여기서 기존 코드처럼 dfs(i, j) == True로 하면 안되는 이유는 그렇다면 조건 자체가 dfs가 실행된 것을 기준으로 하기 때문이다.
            count = 0
            dfs(i,j)
            dimension.append(count)
dimension = sorted(dimension)

print(len(dimension))
for com in dimension:
    print(com, end=' ')

##### 실패 원인 분석: global의 활용과 코드를 따라하는데서 비롯된 원리를 이해하지 못한 것.