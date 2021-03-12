import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dict1 = {}
dict2 = {}


for i in range(n):
    pokemon = input().rstrip()
    dict1[i+1] = pokemon
    dict2[pokemon] = i+1

for _ in range(m):
    x = input().rstrip()
    try:
        x = int(x)
        print(dict1[x])
    except:
        print(dict2[x])