# 16:00 ~ 17:25 1시간 25분 풀었는데 못품..

def solution(n, build_frame):
    answer = []  # [가로좌표, 세로좌표, 0기둥 또는 1보]
    build = [[build_frame[i][0], build_frame[i][1], build_frame[i][2]] for i in range(len(build_frame)) if
             build_frame[i][3] == 1]
    delete = [[build_frame[i][0], build_frame[i][1], build_frame[i][2]] for i in range(len(build_frame)) if
              build_frame[i][3] == 0]
    print('build : ', build)
    print('delete : ', delete)
    # 설치
    for _ in range(len(build)):
        structure = build.pop(0)
        x, y, column_or_beam = structure
        # 보
        if column_or_beam == 1:
            if answer.count([x + 1, y, 1]) > 0 or answer.count([x - 1, y, 1]) > 0 or answer.count(
                    [x, y - 1, 0]) > 0 or answer.count([x + 1, y, 0]) or y != 0:
                answer.append([x, y, column_or_beam])
        # 기둥
        else:
            if answer.count([x + 1, y, 1]) > 0 or answer.count([x - 1, y, 1]) > 0 or answer.count(
                    [x, y - 1, 0]) > 0 or y == 0:
                answer.append([x, y, column_or_beam])
    # 삭제
    for _ in range(len(delete)):
        structure = delete.pop(0)
        x, y, column_or_beam = structure
        if answer.count(structure) == 0:
            continue

        answer.remove([x, y, column_or_beam])
        # 보
        if column_or_beam == 1:
            if (answer.count([x + 1, y, 1]) == 0 and answer.count([x - 1, y, 1]) == 0) or answer.count(
                    [x, y - 1, 0]) > 0 or answer.count([x + 1, y-1, 0]) > 0:
                continue
            else:
                answer.append([x, y, column_or_beam])
        # 기둥
        else:
            if (answer.count([x + 1, y, 1]) > 0 and answer.count([x - 1, y, 1]) > 0) or answer.count(
                    [x, y+1, 0]) == 0:
                continue
            else:
                answer.append([x, y, column_or_beam])
    answer.sort()
    return answer


# [가로좌표, 세로좌표, 0은 기둥, 1은 보, 0은 삭제 1은 설치]


# print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
# print(solution(5, [[5,1,1,1],[5,1,0,1]]))
