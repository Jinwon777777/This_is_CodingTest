n = int(input())

def count(n):
    if n==1:
        return True
    elif n%2 == 0:
        return count(n//2)
    elif n%3 == 0 :
        return count(n//3)
    elif n%5 == 0 :
        return count(n//5)
    else:
        return False

stacked = 0
num = 0

while stacked < n:
    num += 1
    if count(num):
        stacked += 1

print(num)