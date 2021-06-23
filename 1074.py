n,r,c = map(int, input().split())

num=0

while n>0:
    t = (2 ** n) // 2
    if n>1:
        if r >= t and c >= t:
            num += (t**2)*3
            c-=t
            r-=t
        elif r< t and c >= t:
            num += (t**2)
            c-=t
        elif r>= t and c < t:
            num +=  (t**2)*2
            r-=t
    elif n==1:
        if r==0 and c == 1:
            num+=1
        elif r==1 and c==0:
            num+=2
        elif r==1 and c==1:
            num+=3
    n-=1

print(num)
