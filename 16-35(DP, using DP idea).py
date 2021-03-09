n = int(input())

dp = [0]*n

dp [0] = 1

i2= i3 = i5 = 0

next2, next3, next5 = 2,3,5

### idea는 작은 수 부터 못생긴 수를 찾아서 채워넣는것.
### 구현은 못생긴 수를 찾으면 작은 수 부터 들어가는데 찾은 못생긴 수에 못생긴 수를 곱하면 못생긴 수 라는 것에 착안.
for i in range(1,n):
    dp[i] = min(next2, next3, next5)
    if dp[i] == next2:
        i2+=1
        ### 이는 못생긴 수를 작은 순 부터 찾아서 곱해넣는것.
        next2 = dp[i2]*2
    ### elif가 아닌 if인 이유는 같아도 상관없기 때문. dp에 들어간 건 한번 들어갔고 업데이트를 같은 수 모두에게 해주어야하기 때문
    if dp[i] == next3:
        i3+=1
        next3 = dp[i3]*3

    if dp[i] == next5:
        i5+=1
        next5 = dp[i5]*5

print(dp[n-1])