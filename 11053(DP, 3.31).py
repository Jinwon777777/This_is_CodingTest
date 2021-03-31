n = int(input())

num = list(map(int, input().split()))

dp = [0] * (n)

dp[0] = (num[0], 1)

for i in range(1, n):
    max_num = 0
    for j in range(i-1, -1, -1):
        if dp[j][0] < num[i]:
            max_num = max(max_num, dp[j][1])
    dp[i] = (num[i], max_num+1)

ans = 0
for com in dp:
    ans = max(ans, com[1])

print(ans)
