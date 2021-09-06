# 브루트포스는 생각보다 더 무식하게 하자.

n = int(input())

count = 0

giv_str = 666

while True:
    if '666' in str(giv_str):
        count += 1
    if count == n:
        break
    giv_str += 1
print(giv_str)
