"""
数独: 玩家需要根据9x9盘面上的已知数字, 推理出所有剩余空格的数字, 并满足每一行、每一列、每一个粗线宫内的数字均含1-9, 不重复.
保证输入的数独是合法的, 且有唯一解.
输入描述:
输入9行, 每行9个整数, 使用空格分隔. 数字为0-9, 0表示空格.
输出描述:
输出9行, 每行9个整数, 使用空格分隔, 表示完整的解
"""
def is_valid(board, row, col, num): # 检查某个数字是否可以合法地填入指定的位置
    # 检查行
    for i in range(9):
        if board[row][i] == num:
            return False
    # 检查列
    for i in range(9):
        if board[i][col] == num:
            return False
    # 检查3x3宫格
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board): # 数独求解函数, 使用回溯法解决数独问题
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve(board):
                            return True
                        board[i][j] = 0 # 回溯, 撤销当前填充的数字,尝试其他数字
                return False
    return True

if __name__ == "__main__":
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))
    solve(board)
    for row in board:
        print(' '.join(map(str, row)))