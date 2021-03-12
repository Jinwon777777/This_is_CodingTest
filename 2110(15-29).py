n, c = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(int(input()))

arr = sorted(arr)

start = 1
end = arr[-1]-arr[0]
result = 0

while start<=end:
    mid = (start+end)//2
    val = arr[0]
    count = 1
    for i in range(1,n):
        if arr[i] >= val + mid:
            count+=1
            val = arr[i]
    ### 설치 개수가 c보다 많으면 더 들어갈 수도 있으니 mid를 더 크게 해야
    if count >= c:
        start = mid+1
        result = mid
    else:
        end = mid-1

print(result)