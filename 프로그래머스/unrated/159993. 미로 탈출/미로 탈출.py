from collections import deque


def bfs(i, j, n, m, maps, target) -> list:
    queue = deque()
    queue.append((i, j))
    visited = [[-1] * m for _ in range(n)]
    visited[i][j] = 0
    while queue:
        y, x = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_x = dx + x
            next_y = dy + y
            if -1 < next_x < m and -1 < next_y < n and maps[next_y][next_x] != 'X' and visited[next_y][next_x] == -1:
                visited[next_y][next_x] = visited[y][x] + 1
                if maps[next_y][next_x] == target:
                    return [next_y, next_x, visited[next_y][next_x]]
                queue.append((next_y, next_x))
    return [-1, -1, -1]
                
    

def solution(maps) -> int:
    answer = 0
    n, m = len(maps), len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                lever_y, lever_x, count1 = bfs(i, j, n, m, maps, 'L')
                if count1 == -1:
                    return -1
                exit_y, exit_x, count2 = bfs(lever_y, lever_x, n, m, maps, 'E')
                if count2 == -1:
                    return -1
                return count1 + count2