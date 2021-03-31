obj = int(input())
n = int(input())

button = []
for i in range(10):
    button.append(str(i))
if n != 0:
    brk = list(input().split())
    button = [x for x in button if x not in brk]

min_num = (abs(obj - 100))

for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if num[j] not in button:
            break
        elif j == len(num)-1:
            min_num = min(min_num, abs(int(num) - obj) + len(num))

print(min_num)
