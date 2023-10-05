from collections import deque


def bfs(i, j, board, n, m) -> int:
    visited = [[-1] * m for _ in range(n)]
    visited[i][j] = 0
    queue = deque()
    queue.append((i, j))
    while queue:
        y, x = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_x = dx + x
            next_y = dy + y
            tmp = 2
            while -1 < next_x < m and -1 < next_y < n and board[next_y][next_x] != 'D':
                next_x = dx * tmp + x
                next_y = dy * tmp + y
                tmp += 1
            tmp -= 2
            next_x = dx * tmp + x
            next_y = dy * tmp + y
            if visited[next_y][next_x] != -1:
                continue
            visited[next_y][next_x] = visited[y][x] + 1
            if board[next_y][next_x] == 'G':
                return visited[next_y][next_x]
            queue.append((next_y, next_x))
            
    return -1
    

def solution(board) -> int:
    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                return bfs(i, j, board, n, m)