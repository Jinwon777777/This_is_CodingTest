import sys
import heapq

n = int(input())
h = []
ind = 0
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        try:
            print(heapq.heappop(h))
        except:
            print(0)
    else:
        heapq.heappush(h, x)