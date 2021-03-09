t = int(input())

for _ in range(t):
    m,n,k = map(int, input().split())

    arr = [[0]*n for _ in range(m)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for _ in range(k):
        a,b = map(int, input().split())
        arr[a][b] = 1

    def dfs(x,y):
        ### x, y 에 조건 포함 안하고
        if arr[x][y] == 1:
            arr[x][y] = 2
            for l in range(4):
                hx = x+dx[l]
                hy = y + dy[l]
                if hx >= 0 and hx < m and hy >= 0 and hy < n:
                    dfs(hx, hy)
            return
        else:
            return None

    count = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                count += 1
                dfs(i,j)
    print(count)