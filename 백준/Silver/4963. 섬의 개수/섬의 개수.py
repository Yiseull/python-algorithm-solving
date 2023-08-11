import sys
from collections import deque
input = sys.stdin.readline


def bfs(i, j, w, h, mapp, visited) -> int:
    count = 1
    queue = deque()
    queue.append([i, j])
    visited[i][j] = True
    while queue:
        y, x = queue.popleft()
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < w and 0 <= next_y < h and mapp[next_y][next_x] == 1 and not visited[next_y][next_x]:
                queue.append([next_y, next_x])
                visited[next_y][next_x] = True
                count += 1

    return count


def solution(w, h, mapp):
    answer = 0
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if mapp[i][j] == 1 and not visited[i][j]:
                bfs(i, j, w, h, mapp, visited)
                answer += 1

    print(answer)


if __name__ == '__main__':
    while 1:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        mapp = [tuple(map(int, input().split())) for i in range(h)]
        solution(w, h, mapp)
