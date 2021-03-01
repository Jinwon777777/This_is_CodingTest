### 올바른 괄호 문자열인지 검증
def verify(s):
    count = 0
    for com in s:
        if com == '(':
            count+=1
        elif com == ')':
            count -= 1
        if count < 0:
            return False
    return True

### step 2의 나눠야 하는 인덱스 반환
def divide(s):
    ind = 0
    count = 0
    for com in s:
        if com == '(':
            count += 1
        elif com == ')':
            count -= 1
        if count == 0:
            return ind
        ind += 1

### 괄호 변환
def get_through(s):
    if s == '':
        return ''
    u = s[:divide(s)+1]
    v = s[divide(s)+1:]
    if verify(u):
        return u+get_through(v)
    else:
        new = '(' + get_through(v) + ')'
        u = u[1:-1]
        t = ''
        for item in u:
            if item == '(':
                t += ')'
            elif item == ')':
                t += '('
        return new+t

def solution(p):
    answer = get_through(p)
    return answer

p = input()
print(solution(p))