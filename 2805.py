import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip('\n').split())

tree = list(map(int, input().rstrip('\n').split()))
'''
def binary(x, y):
    h = (x+y)//2
    height = 0
    for t in tree:
        if (t-h) > 0:
            height += t-h
    if height == m:
        return h
    elif height > m:
        binary(h+1, y)
    elif height <m:
        binary(x, h-1)'''
start = 0
end = max(tree)
result = 0

while start <= end:
    h = (start+end)//2
    height = 0
    for t in tree:
        if t>h:
            height += t-h
    if height < m:
        end = h-1
    elif height == m:
        result = h
        break
    else:
        result = h
        start = h+1

print(result)