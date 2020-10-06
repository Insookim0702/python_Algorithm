# 13:18 ~ 14:10(50분) ... 6.7점
# k = 5
# food_times = [2, 1, 2]  # -1
# k = 2
# food_times = [2, 2, 2]  # 3
k = 5
food_times = [3, 1, 2]  # 1
# food_times = [1, 1,1]
# food_times = [1, 1,1,1]
result = 0


def solution(food_times, k):
    answer = 0
    count = 0
    import heapq
    q =[]
    for idx, v in enumerate(food_times):
        heapq.heappush(q, (v, idx+1))
    print(q)
    food_num = len(food_times)
    if sum(food_times) <= k:
        return -1
    while (k + 1) != :
        idx = (count % len(q))
        q[idx][0] -= 1
        if q[idx][0] == 0:
            q.heappop()
            continue


    return idx + 1


# def solution(food_times, k):
#     import heapq
#     if sum(food_times) <= k:
#         return -1
#
#     q = []
#     for i in range(len(food_times)):
#         heapq.heappush(q, (food_times[i], i + 1))
#
#     sum_value = 0
#     previous = 0
#     length = len(food_times)
#     while sum_value + ((q[0][0] - previous) * length) <= k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now - previous) * length
#         length -= 1
#         previous = now
#     result = sorted(q, key=lambda x: x[1])
#     return result[(k - sum_value) % length][1]


print(solution(food_times, k))
