from collections import deque


def dfs(n: int, nodes: list) -> list:
    q = deque([1])
    visited = [-1] * (n + 1)
    visited[1] = 0
    while q:
        v = q.popleft()
        for w in nodes[v]:
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[v] + 1
    return visited


def solution(n: int, edge: list) -> int:
    nodes = [[] for _ in range(n + 1)]
    for a, b in edge:
        nodes[a].append(b)
        nodes[b].append(a)
    visited = dfs(n, nodes)
    
    return len([i for i in visited if i == max(visited)])