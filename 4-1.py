from sys import stdin

n = int(stdin.readline())
routes = stdin.readline().split()
x = 1
y = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
sym = ['L', 'R', 'U', 'D']
for route in routes:
    for i in len(sym):
        if route == sym[i]:
            ax = x+dx[i]
            ay = y+dy[i]
    if ax > n or ax < 1 or ay > n or ay < 1:
        continue
    x = ax
    y = ay

print(x,y)