from collections import deque


def bfs(n, graph, visited, start, v1, v2) -> int:
    q = deque([start])
    visited[start] = True
    count = 0
    while q:
        v = q.popleft()
        count += 1
        for w in graph[v]:
            if (v, w) == (v1, v2) or (v, w) == (v2, v1):
                continue
            if not visited[w]:
                q.append(w)
                visited[w] = True
    return count


def solution(n, wires) -> int:
    answer = 100
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for v1, v2 in wires:
        visited = [False] * (n + 1)
        count = []
        for i in range(1, n + 1):
            if not visited[i]:
                count.append(bfs(n, graph, visited, i, v1, v2))
                if len(count) == 2:
                    if sum(count) == n:
                        answer = min(answer, abs(count[0] - count[1]))
                    break
            
    return answer