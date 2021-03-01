import sys
input = sys.stdin.readline

### KeyIdea는 sorted로 숫자를 정렬하면 같은 문자열로 시작하는 문자열은 길이가 짧은게 길이가 긴 것의 앞에 오기 때문에
### list내 비교를 i번째와 i+1번째만 하면 된다는 것.

def compare(x):
    phone = sorted(x)
    for i in range(len(phone)-1):
        # sorted로 숫자를 정렬하면 같은 문자열로 시작하면 길이가 짧은게 길이가 긴 것의 앞에 옴
        if len(phone[i]) <= len(phone[i+1]) and phone[i] == phone[i+1][:len(phone[i])]:
            return 'NO'
    return 'YES'

t = int(input())

for _ in range(t):
    n = int(input())
    phone = []
    for _ in range(n):
        phone.append(input().rstrip())
    print(compare(phone))