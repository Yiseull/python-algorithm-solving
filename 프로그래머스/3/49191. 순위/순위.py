def solution(n: int, results: list) -> int:
    answer = 0
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    
    for win, lose in results:
        graph[win][lose] = 1
        graph[lose][win] = -1
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j or graph[i][j] != 0:
                    continue
                if graph[i][k] == graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1
                    
    for row in graph:
        if row.count(0) == 2:
            answer += 1
    
    return answer