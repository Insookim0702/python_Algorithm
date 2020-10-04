# 11:04~ 12:13(1시간 9분) 96점... 시간초과
def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[0:step]
        print(prev)
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count > 1 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count > 1 else prev
        answer = min(answer, len(compressed))
    return answer


print(solution('aaaabbabbabb'))


def solution(s):
    l = list(s)
    answer = len(s)
    from collections import deque

    for i in range(1, len(s) // 2 + 1):
        result = []
        result.append(s[:i])
        for j in range(1, len(s)):
            v = s[(j * i):((j * i) + i)]
            if v == '':
                break
            else:
                result.append(v)
        if i > len(s) // 2:
            break
        print(result)
        que = deque(result)
        que.append('')
        previous = que.popleft()
        count = 1
        compressed = ''
        while que:
            after = que.popleft()
            if previous != after:
                if count > 1:
                    compressed += str(count) + previous
                else:
                    compressed += previous
                count = 1
            else:
                count += 1
            previous = after
        answer = min(answer, len(compressed))
    return answer


text = "aabbacc"  # 7
print(solution(text))
# text = "ababcdcdababcdcd"	#9
# text = "abcabcdede"	#8
# print(solution(text))
# text = "abcabcabcabcdededededede"	#14
# print(solution(text))
# text = "xababcdcdababcdcd"	#17
# print(solution(text))
