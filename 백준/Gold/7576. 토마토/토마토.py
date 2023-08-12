import sys
from collections import deque
input = sys.stdin.readline


def bfs(i, j, m, n, box, visited, tomato):
    queue = deque(tomato)
    visited[i][j] = 0

    while queue:
        y, x = queue.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            next_x = dx + x
            next_y = dy + y
            if 0 <= next_x < m and 0 <= next_y < n and box[next_y][next_x] == 0 and (visited[next_y][next_x] == 0 or visited[next_y][next_x] > visited[y][x] + 1):
                queue.append((next_y, next_x))
                visited[next_y][next_x] = visited[y][x] + 1


def solution(m, n, box) -> int:
    visited = [[0] * m for _ in range(n)]

    tomato = []
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1 and visited[i][j] == 0:
                tomato.append((i, j))
    bfs(i, j, m, n, box, visited, tomato)

    for i in range(n):
        for j in range(m):
            if box[i][j] == 0 and visited[i][j] == 0:
                return -1

    return max(map(max, visited))


if __name__ == '__main__':
    m, n = map(int, input().split())
    box = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(m, n, box))
