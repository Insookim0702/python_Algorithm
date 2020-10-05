def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x, y, 1] in answer or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False

        else:  # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '앞 뒤로 보가 있거나'
            if [x, y-1, 0] in answer or [x + 1, y-1, 0] in answer or ([x + 1, y, 1] in answer and [x - 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for i in build_frame:
        x, y, stuff, delete_or_build = i
        unit =[x,y,stuff]
        if delete_or_build == 1:
            answer.append(unit)
            if not possible(answer):
                answer.remove(unit)
                continue
        else:
            answer.remove(unit)
            if possible(answer):
                continue
            else:
                answer.append(unit)
    answer.sort()
    return answer


# [가로좌표, 세로좌표, 0은 기둥, 1은 보, 0은 삭제 1은 설치]
print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
# print(solution(5, [[5,1,1,1],[5,1,0,1]]))
