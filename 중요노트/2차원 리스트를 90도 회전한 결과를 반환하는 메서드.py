def rotate_90_degree_2matrix(key):
    n = len(key)
    rotated_key = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_key[i][j] = key[j][n-i-1]
    print(rotated_key)
    return rotated_key


rotate_90_degree_2matrix([[0, 0, 0], [1, 0, 0], [0, 1, 1]])

