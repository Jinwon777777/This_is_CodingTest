n = int(input())

array = []
for _ in range(n):
    a, b = input().split()
    array.append((a, b))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end =' ')