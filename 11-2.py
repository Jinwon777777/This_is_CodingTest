n = input()

result = int(n[0])

for i in range(1, len(n)):
    result = max(result+int(n[i]), result*int(n[i]))

print(result)