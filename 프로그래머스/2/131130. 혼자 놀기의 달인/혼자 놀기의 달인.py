def dfs(cards, n, i, visited, box) -> None:
    while not visited[i]:
        visited[i] = True
        box.append(i)
        i = cards[i] - 1


def solution(cards) -> int:
    answer = 0
    n = len(cards)
    
    for i in range(n):
        visited = [False] * n
        box1 = []
        dfs(cards, n, i, visited, box1)
        for j in range(n):
            if not visited[j]:
                box2 = []
                dfs(cards, n, j, visited, box2)
                answer = max(answer, len(box1) * len(box2))
                print(len(box1), len(box2))
    
    return answer