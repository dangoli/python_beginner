"""
有一个h行w列的网格, 我们使用(i,j)表示网格从上往下数第i行, 从左往右数第j列的单元格. 每个方格要么是可以通过的空方格'0', 要么是不可通过的障碍物'1'. 特别地, 网格的四周都是墙方格,
你可以沿着空方格上下左右随意移动: 从(x,y)向上移动一格到(x-1,y), 向下移动一格到(x+1,y), 向左移动一格到(x,y-1), 向右移动一格到(x,y+1). 
现在你位于迷宫的入口(0,0), 目标是到达迷宫的出口(h-1,w-1). 请输出一条从起点到终点的可行路径.
保证起点和终点都是空方格, 始终可以找到且唯一能够找到一条从起点出发到达终点的可行路径.
输入描述:
第一行包含两个整数h,w(1≤h,w≤100), 表示网格的行数和列数.
接下来h行, 每行包含一个长度为w的字符串, 仅包含'0'和'1', 表示网格的布局. 
输出描述:
输出若干行, 第i行输出两个整数xi,yi, 表示第i步的行号和列号. 
保证输出的路径是符合题目要求的, 即从起点(0,0)到终点(h-1,w-1)的路径. 且路径上每个单元格都是空方格'0', 行走的单元格都是彼此相邻的.
"""

#!/usr/bin/env python3
import sys

def find_path_dfs_iterative(grid, h, w):
    start = (0, 0)
    target = (h-1, w-1)
    stack = [start] # 栈
    parent = {start: None} # 记录路径
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    while stack:
        x, y = stack.pop()
        if (x, y) == target:
            break
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == '0' and (nx, ny) not in parent:
                parent[(nx, ny)] = (x, y)
                stack.append((nx, ny))
    if target not in parent: # 没有找到路径
        return None
    # 还原路径
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path

def read_grid():
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        s = input().split(" ")
        grid.append(list(s))
    return grid, h, w

def main():
    grid, h, w = read_grid()
    path = find_path_dfs_iterative(grid, h, w)
    if path is None:
        print("No path found", file=sys.stderr)
        return
    for x, y in path:
        print(f"({x},{y})")

if __name__ == "__main__":
    main()