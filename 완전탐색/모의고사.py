def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0] * 3
    k = 0
    length = len(answers)
    for i, v in enumerate(answers):
        if v == student1[i%len(student1)]: score[0] += 1
        if v == student2[i%len(student2)]: score[1] += 1
        if v == student3[i%len(student3)]: score[2] += 1
    result = sorted([(1, score[0]), (2, score[1]), (3, score[2])], key=lambda x: x[1], reverse=True)
    print(result)

    l = [i[0] for i in result if result[0][1] == i[1]]
    return sorted(l)


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
