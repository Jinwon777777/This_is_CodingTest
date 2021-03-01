n = input()
count = 0
for i in range(len(n)-1):
    if n[i] != n[i+1]:
        count += 1

ans = count//2

print(ans)