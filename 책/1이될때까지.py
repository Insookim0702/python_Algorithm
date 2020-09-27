def solution(n, k):
    count = 0
    num = n
    while num != 1:
        if num % k == 0:
            num = num // k
            count+=1
            continue
        num -= 1
        count+=1
    return count


print(solution(25, 5))
print(solution(25, 3))
print(solution(27, 3))
print(solution(9, 3))
print(solution(17, 4))
