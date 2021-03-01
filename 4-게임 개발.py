from sys import stdin

n, m = map(int, stdin.readline().split())

r,c,d = map(int, stdin.readline().split())

a = [list(map(int, stdin.readline().split())) for _ in range(n)]

count = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def clean(r,c,d):
    global count
    if a[r][c] == 0:
        a[r][c] = 2
        count += 1
    for _ in range(4):
        nd = (d+3)%4
        nr = r+dx[nd]
        nc = c+dy[nd]
        if a[nr][nc] == 0:
            clean(nr, nc, nd)
            return
        d = nd
    nd = (d+2) % 4
    nr = r + dx[nd]
    nc = c + dy[nd]
    if a[nr][nc] == 1:
        return
    clean(nr, nc, d)
clean(r,c,d)
print(count)