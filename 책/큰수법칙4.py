def solution(n, m, k, arr):
    arr.sort()
    first = arr[-1]
    second = arr[-2]
    answer = 0
    while True:
        if m == 0:
            break
        for i in range(k):
            if m == 0:
                break
            answer += first
            m-=1
        answer +=second
        m -= 1
    return answer

print(solution(5, 8, 3, [2, 4, 5, 4, 6]))