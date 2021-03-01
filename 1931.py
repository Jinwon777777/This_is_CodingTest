import sys

input = sys.stdin.readline

n = int(input())
conf = []
for _ in range(n):
    h = tuple(map(int, input().split()))
    conf.append(h)
conf = sorted(conf, key= lambda x : x[0])
conf = sorted(conf, key= lambda x : x[1])

value = 0
result = []
for c in conf:
    if c[0] >= value:
        value = c[1]
        result.append(c)
print(len(result))