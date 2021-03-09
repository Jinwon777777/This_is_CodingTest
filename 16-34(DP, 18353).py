n = int(input())

### 숫자
arr = list(map(int, input().split()))
arr.reverse()
### dp는 병사 수
dp = [1]*n

for i in range(1, n):
    ### 값이 크면 dp에 바로 반영
    for j in range(0,i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j]+1, dp[i])


print(n - max(dp))