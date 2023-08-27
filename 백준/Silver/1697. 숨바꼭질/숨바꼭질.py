import sys
from collections import deque
input = sys.stdin.readline


def bfs(n, k) -> int:
    max_range = k * 2
    visited = [-1] * max_range
    visited[n] = 0
    queue = deque([n])
    while queue:
        x = queue.popleft()
        for i in [x + 1, x - 1, x * 2]:
            if -1 < i < max_range and visited[i] == -1:
                queue.append(i)
                visited[i] = visited[x] + 1
                if i == k:
                    break

    return visited[k]


if __name__ == '__main__':
    n, k = map(int, input().split())
    if n < k:
        print(bfs(n, k))
    else:
        print(n - k)
