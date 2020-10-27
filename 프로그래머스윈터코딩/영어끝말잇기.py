from collections import deque


def solution(n, words):
    answer = [0,0]
    que = deque()
    words.insert(0, 0)
    # 4:28 ~ 4:58
    for i in range(1, len(words)):
        if words[i] in words[1:i] or (i >1 and words[i-1][-1] != words[i][0]):
            pe = int(i % n)
            if pe == 0:
                pe = n
            answer[0] = pe
            answer[1] = i // n
            if i%n !=0:
                answer[1] +=1
            return answer
    return answer


print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
print(solution(5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang','gather', 'refer', 'reference', 'estimate', 'executive']))
print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))
