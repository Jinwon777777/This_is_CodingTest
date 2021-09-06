from collections import deque

n = int(input())

ans = deque()
test1 = deque()
test2 = deque()

for _ in range(n):
    x, y = input().split()
    if not ans:
        ans.append((int(x), y))
    else:
        test2 = ans
        while test2:
            h1 = test2.popleft()
            if h1[0] > int(x):
                test1.append((int(x), y))
                test1.append(h1)
                test1.extend(test2)
                break
            elif h1[0] <= int(x) and not test2:
                test1.append(h1)
                test1.append((int(x), y))
            else:
                test1.append(h1)
        ans = test1
        test1 = deque()
        test2 = deque()

for pair in ans:
    print("{0} {1}".format(pair[0], pair[1]))
