# 13:18 ~ 14:10(50분) ... 6.7점
k = 31
food_times = [1, 5, 5, 5, 5, 6, 7] #1
#k = 5
#food_times = [3, 1,3] #3
#food_times = [1, 1,1]
#food_times = [1, 1,1,1]
result = 0

def solution(food_times, k):
    answer = 0
    count = 0
    food_num = len(food_times)
    if sum(food_times) <= k:
        return -1
    while (k+1) != count:
        idx = (count % food_num)
        count += 1
        if food_times[idx] == 0:
            continue
        food_times[idx] -= 1
    idx = (count % food_num)
    return idx+1


print(solution(food_times, k))
