import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))
prov = list(map(int, input().rstrip('\n').split()))
m = int(input().rstrip('\n'))

start = 0
end = max(prov)
max_amount = 0
while start <= end:
    mid = (start+end)//2
    total = 0
    for p in prov:
        if p > mid:
            total += mid
        else:
            total += p
    if total == m:
        max_amount = mid
        break
    elif total > m:
        end = mid-1
    else:
        max_amount = mid
        start = mid+1


print(max_amount)