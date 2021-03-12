from collections import deque

m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0 ,0]
dy = [0,0,-1,1]

q = deque()
s = 0

# q에 익은 토마토 위치와 시간 저장
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i,j,s])

while q:
    x, y, ds = q.popleft()
    s = max(ds, s)
    for k in range(4):
        hx = x+dx[k]
        hy = y + dy[k]
        if hx >= 0 and hx < n and hy >= 0 and hy < m and arr[hx][hy] == 0:
            arr[hx][hy] = 1
            q.append([hx, hy, ds+1])

rott = False
for i in range(n):
    if rott == True:
        break
    for j in range(m):
        if arr[i][j] == 0:
            rott = True
            break

if rott:
    print(-1)
else:
    print(s)
