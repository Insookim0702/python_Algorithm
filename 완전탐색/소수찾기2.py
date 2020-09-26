from itertools import permutations
import math
def solution(numbers):
    li = list(numbers)
    l = set();
    answerCount = 0;
    for i in range(2, len(numbers)+1):
        list1 = list(permutations(li, i))
        m = ''
        for ss in list1:
            for s in ss:
                m+=s
            l.add(m)
            m=''

    for val in l:
        issosu = True
        if val[0] != '0' and val != '1':
            for index in range(2, int(math.sqrt(int(val)))+1):
                if int(val) % index == 0 :
                    issosu = False
                    break
            if issosu == True :
                answerCount+=1
    return answerCount


print(solution("011"))