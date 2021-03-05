n = int(input())
s = []

for _ in range(n):
    s.append(list(map(int, input().split())))

dp = [0]*n
if s[n-1][0] == 1:
    dp[n-1] = s[n-1][1]
else:
    dp[n-1] = 0

for i in range(n-2,-1,  -1):
    if s[i][0] > n-i:
        dp[i] = 0
    elif s[i][0] == n-i:
        dp[i] = s[i][1]
    else:
        max_num = dp[n-1]
        for v in range(i+s[i][0], n-1):
            max_num = max(dp[v], max_num)
        dp[i] = max_num + s[i][1]


print(max(dp))