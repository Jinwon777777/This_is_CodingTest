n = int(input())

ind0 = [1,0]
ind1 = [0,1]

for i in range(2, 41):
    ind0.append(ind0[i-2]+ind0[i-1])
    ind1.append(ind1[i-2]+ind1[i-1])

for _ in range(n):
    num = int(input())
    print(ind0[num], ind1[num])