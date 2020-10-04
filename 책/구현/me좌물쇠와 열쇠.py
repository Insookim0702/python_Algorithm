
def solution(key, lock):
    n = len(key)
    m = len(lock)
    new_l = [[0] * (m * 3) for _ in range(m*3)]
    for i in range(m):
        for j in range(m):
            new_l[i+m][j+m] = lock[i][j]
    print(new_l)
    for i in range(4):
        new_lock = new_l
        for x in range(m*2):
            for y in range(m*2):
                for i in range(n):
                    for j in range(n):
                        new_lock[x+i][y+j] = key[i][j]
                if check(new_lock):
                    return True
        key = rotate_90_degree_matrix(key)
        print(key)
    return False

def check(new_lock):
    n =  len(new_lock) // 3
    for i in range(n, n *2):
        for j in range(n, n*2):
            if new_lock[i][j] != 1:
                return False
    return True

def rotate_90_degree_matrix(key):
    n = len(key)
    rotated_key = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_key[i][j] = key[j][n-i-1]
    return rotated_key




print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))  # true