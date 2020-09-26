def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for x in range(0, len(answers)):
        if pattern1[x % 5] == answers[x]: score[0] += 1
        if pattern2[x % 8] == answers[x]: score[1] += 1
        if pattern3[x % 10] == answers[x]: score[2] += 1
    print(score)
    mx = max(score)
    return [idx + 1 for idx, val in enumerate(score) if val == mx]


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
