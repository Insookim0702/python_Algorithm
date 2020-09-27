def solution(n, m, arr):
    answer = ''
    # 20:30~
    l = sorted(arr, reverse=True)
    print(l)
    for i in range(1, n + 1):
        if m ==0:
            break
        if i % (m + 1) == 0:
            answer += str(l[1]) + '+'
        else:
            answer += str(l[0]) + '+'
    print(answer)
    return eval(answer[:len(answer) - 1])


print(solution(8, 3, [2, 4, 5, 4, 6]))
print(solution(8, 3, [2, 4, 5, 4, 6]))
