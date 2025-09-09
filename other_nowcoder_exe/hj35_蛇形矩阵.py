def snake_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    m = 1
    for p in range(n):
        for i in range(p + 1)[::-1]:
            j = p - i
            matrix[i][j] = m
            m += 1
    return matrix

# 示例
n = int(input())
matrix = snake_matrix(n)
for i in range(n):
    for j in range(n - i):
        print(matrix[i][j], end=' ')
    print()