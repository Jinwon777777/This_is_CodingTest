n = int(input())

judge = []
for _ in range(n):
    age, name = map(str, input().split())
    judge.append((int(age), name))

sorted_judge = sorted(judge, key=lambda person: (person[0]))

for al in sorted_judge:
    print(str(al[0]) + ' ' + al[1])
