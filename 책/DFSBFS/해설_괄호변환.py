# 21:32 ~ 22:52
# 균형잡힌 괄호 문자열
def balanced_str(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check_perfect(p):
    count =0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
               return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_str(p)
    u = p[:index+1]
    v = p[index+1:]
    if check_perfect(u):
        return u + solution(v)
    else:
        an = '('
        an += solution(v)
        an += ')'
        l = list(u[1:-1])
        for i in range(len(l)):
            if l[i] == ')':
                l[i] = '('
            else:
                l[i] = ')'

        return an + ''.join(l)
    return answer

print(solution("(()())()"))  # "(()())()"
print(solution(")("))  # "()"
print(solution("()))((()"))  # "()(())()"