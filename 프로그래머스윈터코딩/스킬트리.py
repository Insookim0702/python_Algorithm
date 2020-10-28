# 3:29 ~3:48
def solution(s, skill_trees):
    answer = 0
    skill_step = list(s)
    for skill_tree in skill_trees:
        answer += 1
        temp_str = ''
        for i in skill_tree:
            if i in skill_step:
                temp_str += i
        print(temp_str)
        for i in range(len(temp_str)):
            if temp_str[i] != s[i]:
                answer-=1
                break

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
