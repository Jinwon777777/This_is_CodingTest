t = int(input())
### 이전 인덱스에 더하기 위해
d = [-1, 0, 1]
for _ in range(t):
    n, m = map(int, input().split())
    proto = list(map(int, input().split()))
    start, end = 0, m
    arr = []
    for _ in range(n):
        arr.append(proto[start:end])
        start += m
        end += m
    dp = [[0]*n for _ in range(m)]

    for num in range(n):
        dp[0][num] = arr[num][0]

    for i in range(1, m):
        for j in range(n):
            h = []
            for k in range(3):
                if j+d[k] >= 0 and j+d[k] < n:
                    h.append(dp[i-1][j+d[k]])
            dp[i][j] = max(h) + arr[j][i]

    print(max(dp[m-1]))