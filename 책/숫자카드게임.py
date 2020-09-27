def solution(n, m, arr):
    answer = [0] * len(arr)
    for i in range(len(arr)):
        answer[i] = min(arr[i])
    return max(answer)


print(solution(3, 3, [[3, 1, 2], [4, 1, 4], [2, 2, 2]]))
print(solution(3, 4, [[7, 3, 1, 8], [3, 3, 3, 4]]))
