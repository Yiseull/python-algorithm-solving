from collections import deque


def bfs(i, j, place) -> bool:
    queue = deque()
    queue.append((i, j))
    visited = [[False] * 5 for _ in range(5)]
    visited[i][j] = True
    while queue:
        y, x = queue.pop()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_x = dx + x
            next_y = dy + y
            if -1 < next_x < 5 and -1 < next_y < 5 and abs(i - next_y) + abs(j - next_x) < 3 and place[next_y][next_x] != 'X' and not visited[next_y][next_x]:
                if place[next_y][next_x] == 'P':
                    return False
                queue.append((next_y, next_x))
                visited[next_y][next_x] = True
    return True


def check(place) -> int:
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P' and not bfs(i, j, place):
                return 0
    return 1


def solution(places) -> list:
    answer = [0] * 5
    for i, place in enumerate(places):
        answer[i] = check(place)
    return answer