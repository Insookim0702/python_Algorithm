def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * n * 3 for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    for _ in range(4):
        key = rotate_90_degree_2matrix(key)
        for x in range(n * 2):
            for y in range(n * 2):

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check_all_1(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False


def check_all_1(new_lock):
    n = len(new_lock) // 3
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def rotate_90_degree_2matrix(key):
    n = len(key)
    rotated_key = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_key[i][j] = key[j][n - i - 1]
    return rotated_key
