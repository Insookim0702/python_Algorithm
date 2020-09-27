def solution(n, m, k, arr):
    # 66656665
    arr.sort()
    first = arr[-1]
    second = arr[-2]
    count = int(m / (k + 1)) * k
    count += m % (k + 1)
    return (count * first) + ((m - count) * second)


print(solution(5, 8, 3, [2, 4, 5, 4, 6]))
