def solution(answers):
    p= [[1, 2, 3, 4, 5]
    ,[2, 1, 2, 3, 2, 4, 2, 5]
    ,[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for idx, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[idx % len(v)]:
                s[i] +=1
    return [i+1 for i, v in enumerate(s) if v == max(s)]

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
