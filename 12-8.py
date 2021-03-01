n = input()
n = sorted(n)
num = 0
count = 0
for s in n:
    if s in '1234567890':
       num += int(s)
       count+=1
    else:
        break

sorted_n = n[count:]
sorted_n.append(str(num))
joined_n = ''.join(sorted_n)
print(joined_n)