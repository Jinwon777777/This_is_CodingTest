from sys import stdin
n = int(input())

arr = []
ans = []

for i in range(n):
  x = list(map(int, input().split()))
  arr.append(x)

ans.append(arr[0])
ans.append([arr[0][0]+arr[1][0], arr[0][0]+arr[1][1]])

for j in range(2, n):
  temp = []
  temp.append(ans[j-1][0]+arr[j][0])
  for k in range(1,j):
    num = max(ans[j-1][k-1], ans[j-1][k])+arr[j][k]
    temp.append(num)
  temp.append(ans[j-1][-1]+arr[j][-1])
  ans.append(temp)

result = max(ans[n - 1])
print(result)
