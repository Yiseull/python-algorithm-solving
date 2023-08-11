import sys
from collections import deque
input = sys.stdin.readline


def bfs(n, computers) -> int:
    count = 0
    q = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True

    while q:
        v = q.popleft()
        for i in computers[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                count += 1

    return count


if __name__ == '__main__':
    n = int(input())
    computers = [[] for _ in range(n + 1)]
    for _ in range(int(input())):
        a, b = map(int, input().split())
        computers[a].append(b)
        computers[b].append(a)

    print(bfs(n, computers))