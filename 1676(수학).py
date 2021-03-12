n = int(input())

count5 = 0

for i in range(1, n+1):
    x = i
    while x%5 == 0:
        x = int(x//5)
        count5+=1

print(count5)