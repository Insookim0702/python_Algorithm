# 15:42 ~ 16:33 50분 풀엇는데, 못 품

from collections import deque


def check(que):
    que = deque(que)
    pre = que.popleft()
    m = []
    if pre == ')':
        return False
    m.append(pre)
    while que:
        aft = que.popleft()
        if aft == ')':
            m.pop()
        else:
            m.append(aft)
    if len(m) == 0:
        return True
    else:
        return False


def dfs(u, v):
    l = list(v)
    if check(l):
        u += v
        return u, v
    temp = ''
    m = []
    count = 0
    for i in l:
        count += 1
        temp += i
        if i == '(':
            m.append('(')
        else:
            m.pop()

        if m:
            u += temp
            v = ''.join(l[count:])
            if v == '':
                return u, v
            dfs(u, v)

    return u, v


def solution(p):

    u, v = dfs('', p)
    return u


#print(solution("(()())()"))  # "(()())()"
print(solution(")("))  # "()"
#print(solution("()))((()"))  # "()(())()"
