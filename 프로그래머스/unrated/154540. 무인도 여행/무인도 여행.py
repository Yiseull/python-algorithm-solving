from collections import deque


def bfs(i, j, maps, visited, n, m) -> int:
    queue = deque([(i, j)])
    visited[i][j] = True
    count = int(maps[i][j])
    while queue:
        y, x = queue.pop()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_x = x + dx
            next_y = y + dy
            if -1 < next_x < m and -1 < next_y < n and maps[next_y][next_x] != 'X' and not visited[next_y][next_x]:
                queue.append((next_y, next_x))
                visited[next_y][next_x] = True
                count += int(maps[next_y][next_x])
                
    return count
    



def solution(maps) -> list:
    answer = []
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j, maps, visited, n, m))
    return sorted(answer) if answer else [-1]