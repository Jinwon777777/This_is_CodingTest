def solution(s):
    res = []
    result = ''
    if len(s) == 1:
        return 1
    for c in range(1, len(s)//2+1):
        temp = s[:c]
        count = 1
        for i in range(c,len(s), c):
            if s[i:i+c] == temp:
                count += 1
            else:
                if count == 1:
                    count = ''
                result += str(count) + temp
                temp = s[i:i+c]
                count = 1
        if count == 1:
            count = ''
        result += str(count) + temp
        res.append(len(result))
        result = ''
    answer = min(res)
    return answer

print(solution('adfdfdfdfddffff'))