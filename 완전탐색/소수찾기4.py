from itertools import permutations
import math
def solution(n):
    s = set()
    for i in range(len(n)):
        case = list(map(''.join, permutations(n, i+1)))
        for j, value in enumerate(case):
            s.add(int(value))
    values = list(s)
    print(values)
    count = 0
    for val in values:
        if val != 1 and val !=0:
            isPrime = True

            for i in range(2, int(math.sqrt(val))+1):
                if val % i == 0 :
                    isPrime = False
                    break
            if isPrime :
                count+=1

    return count

print(solution("17"))
print(solution("011"))