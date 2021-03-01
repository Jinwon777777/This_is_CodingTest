import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input().rstrip()))

# 시간복잡도 줄이기 위해 largest, smallest 함수 만들어 구함.
def largest(arr):
    second = largest = -float('inf')

    for n in arr:
        if n > largest:
            second = largest
            largest = n
        elif second > n >= largest:
            second = n
    return largest, second

def smallest(arr):
    second = smallest = float('inf')

    for n in arr:
        if n < smallest:
            second = smallest
            smallest = n
        elif smallest <= n < second:
            second = n
    return smallest, second

a = sum(arr)

