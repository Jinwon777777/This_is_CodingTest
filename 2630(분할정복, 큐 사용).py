from collections import deque
n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

q = deque()
blue = 0
white = 0

q.append((0,0, n))
### div는 점 두개를 넣어서 잘라도 되면 자르고 count까지 함. 잘라도 되면 True, 아니면 False 반환
def div(x1,y1, n):
    global blue, white
    x2, y2 = x1+n, y1+n
    color = arr[y1][x1]
    for i in range(y1, y2):
        for j in range(x1, x2):
            if arr[i][j] != color:
                return False
    if color == 0:
        white+=1
    else:
        blue+=1
    return True

while q:
    x,y, num = q.popleft()
    if not div(x,y, num):
        num = int(num/2)
        q.append((x, y, num))
        q.append((x+num, y, num))
        q.append((x, y+num, num))
        q.append((x+num, y+num, num))

print(white)
print(blue)
