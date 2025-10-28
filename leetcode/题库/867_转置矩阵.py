matrix = [[1,2,3],[4,5,6],[7,8,9]]
m = len(matrix)
n = len(matrix[0])
ma = [[] for _ in range(n)]
for i in range(n):
    for j in range(m):
        ma[j].append(matrix[i][j])
print(ma)
# print(matrix[0][0])