n = input()

ind = len(n)//2

left = 0
right = 0

for i in range(ind):
    left += int(n[i])
    right += int(n[-1-i])

if left == right:
    print('LUCKY')
else:
    print('READY')