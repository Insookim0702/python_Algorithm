# 15:13 ~ 15:55


def solution(food_times, k):
    answer = 0
    time = 0
    n = len(food_times)
    ar = []
    for idx, v in enumerate(food_times):
        ar.append((v, idx+1))
    ar.sort()
    print(ar)
    return -1

print(solution([3, 1, 2], 5))