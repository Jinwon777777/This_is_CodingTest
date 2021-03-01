from collections import deque

n, k = map(int, input().split())

graph = []
virus = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            ### 값, 시간, 위치
            virus.append([graph[i][j], 0, i, j])
virus.sort()
### 값 순대로 virus가 q에 저장
q = deque(virus)

target_s, target_x, target_y = map(int, input().split())

### 전부다 채운다는 마음가짐
### 종료조건이 큐가 다 비거나(더 이상 채울 곳 없을때) s초에 도달하거나!
while q:
    v, s, x, y = q.popleft()
    if s == target_s:
        break
    for c in range(4):
        nx = x + dx[c]
        ny = y + dy[c]
        if 0<= nx and nx < n and 0<= ny and ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = v
            q.append([v, s+1, nx, ny])

print(graph[target_x-1][target_y-1])