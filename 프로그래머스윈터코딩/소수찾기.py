from itertools import combinations


def is_prime(num):
    for i in range(2,num):
        if num % i ==0:
            return False
    return True


def solution(nums):
    answer = 0
    # 4:17~ 4:28

    com = combinations(nums, 3)
    for i in com:
        print(i)
        sc = sum(i)
        if (sc != 0 or sc != 1) and is_prime(sc):
            answer +=1
    return answer


print(solution([1, 2, 3, 4]))  # 1
print(solution([1, 2, 7, 6, 4]))  # 4
