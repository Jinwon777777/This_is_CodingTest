n = input()
x = int(ord(n[0]))-int(ord('a'))+1
y = int(n[1])
count = 0
steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,-2), (1,2), (-1,-2), (-1,2)]

for step in steps:
    ax = x + step[0]
    ay = y + step[1]
    if ax > 8 or ax < 1 or ay >8 or ay<1:
        continue
    count+=1

print(count)