def solution(d, budget):
    answer = 0
    d.sort()
    print(d)
    for i in d:
        if budget >= i:
            budget -= i
            answer += 1
        else:
            return answer
    return answer


# 5:10 ~ 5:18
print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))