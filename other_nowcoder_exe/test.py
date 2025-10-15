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
