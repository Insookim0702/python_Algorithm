def solution(answers):
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a1p = 0
    a2p = 0
    a3p = 0
    k = 0
    length = len(answers)
    for i in a1:
        if i == answers[k]:
            a1p += 1
        k +=1
        if k == length:
            k = 0
    k = 0
    i = 0
    for i in a2:
        if i == answers[k]:
            a2p += 1
        k += 1
        if k == length:
            k = 0
    k = 0
    i = 0
    for i in a3:
        if i == answers[k]:
            a3p += 1
        k += 1
        if k == length:
            k = 0
    a = [a1p, a2p, a3p]
    result = sorted([(1, a1p), (2, a2p), (3, a3p)], key = lambda x: x[1], reverse=True)
    print(result)

    l = [i[0] for i in result if result[0][1] == i[1]]
    return sorted(l)


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
