from collections import deque
n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

blue = 0
white = 0

def div(x1,y1, n):
    global blue, white
    x2, y2 = x1+n, y1+n
    color = arr[y1][x1]
    for i in range(y1, y2):
        for j in range(x1, x2):
            if arr[i][j] != color:
                n = int(n/2)
                div(x1, y1, n)
                div(x1+n, y1, n)
                div(x1, y1+n, n)
                div(x1+n, y1+n, n)
                return
    if color ==0:
        white+=1
    else:
        blue+=1

div(0,0,n)
print(white)
print(blue)