def s(n, m, c,map):
    now_position = [c[0],c[1],c[2]]
    answer = 0
    dx =[-1,0,1,0]
    dy = [0,1,0,-1]
    #13:45~

    if now_position[2] ==0:
        print(map[c[0]-1][c[1]])
        print(map[c[0]][c[1]-1])
        print(map[c[0]+1][c[1]])
        print(map[c[0]][c[1]+1])
    if now_position[2] ==1:
        print(map[c[0]-1][c[1]])
        print(map[c[0]][c[1]-1])
        print(map[c[0]+1][c[1]])
        print(map[c[0]][c[1]+1])
        c_ = map[now_position[0] + 1][now_position[1]]
        print(c_)
        if c_ == 0:
            map[now_position[0]][now_position[1]] = 2
            answer += 1
            now_position[0] += 1
            now_position[2] = 0
        else:
            now_position[2] = 0

    if now_position[2] ==2:
        c_ = map[now_position[0] + 1][now_position[1]]
        print(c_)
        if c_ ==0 :
            map[now_position[0]][now_position[1]] = 1
            answer +=1
            now_position[0] += 1
            now_position[2] = 1
        else :
            now_position[2] = 1


        print(map[c[0]][c[1]-1])
        print(map[c[0]+1][c[1]])
        print(map[c[0]][c[1]+1])
    if c[2] ==3:
        print(map[c[0]-1][c[1]])
        print(map[c[0]][c[1]-1])
        print(map[c[0]+1][c[1]])
        print(map[c[0]][c[1]+1])

    return np

print(s(4, 4, [1, 1, 0], [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]))