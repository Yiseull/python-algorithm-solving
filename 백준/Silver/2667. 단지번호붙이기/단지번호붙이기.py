import sys
from collections import deque
input = sys.stdin.readline


def bfs(n, mapp, i, j, visited) -> int:
    count = 1
    queue = deque()
    queue.append([i, j])
    visited[i][j] = True
    while queue:
        y, x = queue.popleft()
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < n and 0 <= next_y < n and mapp[next_y][next_x] == '1' and not visited[next_y][next_x]:
                queue.append([next_y, next_x])
                visited[next_y][next_x] = True
                count += 1

    return count


def solution(n, mapp):
    answer = []
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if mapp[i][j] == '1' and not visited[i][j]:
                answer.append(bfs(n, mapp, i, j, visited))

    print(len(answer))
    print('\n'.join(map(str, sorted(answer))))


if __name__ == '__main__':
    n = int(input())
    mapp = [input().rstrip() for _ in range(n)]
    solution(n, mapp)