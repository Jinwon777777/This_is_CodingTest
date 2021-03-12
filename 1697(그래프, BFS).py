from collections import deque
n, k = map(int, input().split())

q = deque()
check = [0]*(100001)
q.append((n, 0))

while True:
    dn, ds = q.popleft()
    check[dn] = 1
    if dn == k:
        break
    if (dn-1) >=0 and (dn-1) <=100000 and check[dn-1] == 0:
        q.append((dn-1, ds+1))
    if (dn + 1) >= 0 and (dn + 1) <= 100000 and check[dn+1] == 0:
        q.append((dn+1, ds+1))
    if 2*dn >= 0 and 2*dn <=100000 and check[2*dn] == 0:
        q.append((2*dn, ds+1))

### 반복문 쓸때 for next in (dn-1, dn+1, 2*dn): 이런 식으로 쓸 수도 있음.
print(ds)