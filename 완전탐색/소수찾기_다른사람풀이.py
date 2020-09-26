from itertools import permutations
import math
def solutions(n):
    test_number = []
    for i in range(len(n)):
        case = list(set(map(''.join, permutations(n, i + 1))))
        for j, number in enumerate(case):
            test_number.append(int(number))
    li =list(set(test_number));

    if li.count(0) != 0:
        li.remove(0)
    count = 0
    for val in li:
        issosu = True
        if val != 1 and val != 0:
            for li in range(2, int(math.sqrt(val))+1):
                if val % li == 0:
                    issosu =False
                    break
            if issosu:
                count +=1

    return count


print(solutions("011"))
print(solutions("17"))

