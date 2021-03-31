n = int(input())

num = list(map(int, input().split()))

dp_left = [0] * n
dp_right = [0] * n

dp_left[0] = (num[0], 1)
for i in range(1, n):
    max_num = 0
    for j in range(i - 1, -1, -1):
        if dp_left[j][0] < num[i]:
            max_num = max(max_num, dp_left[j][1])
    dp_left[i] = (num[i], max_num + 1)

dp_right[-1] = (num[-1], 1)
for i in range(n-1, -1, -1):
    max_num2 = 0
    for j in range(i+1, n):
        if dp_right[j][0] < num[i]:
            max_num2 = max(max_num2, dp_right[j][1])
    dp_right[i] = (num[i], max_num2 + 1)

ans = []
for k in range(n):
    ans.append(dp_left[k][1] + dp_right[k][1] - 1)

print(max(ans))
