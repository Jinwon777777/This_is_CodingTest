from collections import deque

m, n, h = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0 ,0, 0, 0]
dy = [0,0,-1,1, 0, 0]
dz = [0,0, 0, 0,-1,1]

q = deque()
s = 0

# q에 익은 토마토 위치와 시간 저장
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 1:
                q.append([k,i,j,s])

while q:
    z, x, y, ds = q.popleft()
    s = max(ds, s)
    for k in range(6):
        hz = z+dz[k]
        hx = x+dx[k]
        hy = y + dy[k]
        if hx >= 0 and hx < n and hy >= 0 and hy < m and hz>=0 and hz<h and arr[hz][hx][hy] == 0:
            arr[hz][hx][hy] = 1
            q.append([hz, hx, hy, ds+1])

rott = False
for k in range(h):
    if rott == True:
        break
    for i in range(n):
        if rott == True:
            break
        for j in range(m):
            if arr[k][i][j] == 0:
                rott = True
                break

if rott:
    print(-1)
else:
    print(s)