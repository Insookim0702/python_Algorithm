# 16:10 ~

def solution(s):
    answer = 0
    n = len(s)
    min_value = 1e9
    arr = list(s)

    for i in range(1, (n//2)+1):
        result  = ''
        count = 1
        for j in range(n):
            if s[j:i] == s[(j+i):(j+i)+ i]:
                count +=1
                continue
            else:
                if count > 1:
                    result += str(count) + s[j:i]
        print(result)






    return answer

print(solution("aabbaccc"	)) # 7
#print(solution("ababcdcdababcdcd")) # 	9
#print(solution("abcabcdede")) #8
#print(solution("abcabcabcabcdededededede")) # 	14
#print(solution("xababcdcdababcdcd")) # 17