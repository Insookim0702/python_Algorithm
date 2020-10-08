# 13:17 ~ 13:52 35분

def solution(N, stages):
    answer = []
    fail = []
    n = len(stages)
    for i in range(1, N+1):
        count = 0
        mit = 0
        for j in range(n):
            if i ==stages[j]:
                count += 1
            if i <= stages[j]:
                mit += 1
        if count == 0:
            fail.append((0,i))
        else:
            fail.append(((count/mit), i))
    fail.sort(key = lambda x : (-x[0], x[1]))
    print(fail)
    for i in fail:
        answer.append(i[1])
    return answer


def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1, N+1):
        count = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = count / length
        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key= lambda x : x[1], reverse=True)
    print(answer)
    answer = [i[0] for i in answer]
    return answer




print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))