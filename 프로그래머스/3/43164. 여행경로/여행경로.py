from collections import defaultdict


def solution(tickets: list) -> list:
    n = len(tickets)
    tickets_dict = defaultdict(list)
    
    for start, end in tickets:
        tickets_dict[start].append(end)
        
    for key in tickets_dict.keys():
        tickets_dict[key].sort()
        
    def dfs(start: int, cnt: int) -> None:
        if cnt == n:
            return [start]
        for i, city in enumerate(tickets_dict[start]):
            if city == '':
                continue
            tickets_dict[start][i] = ''
            result = dfs(city, cnt + 1)
            tickets_dict[start][i] = city
            if result != -1:
                return [start] + result
        return -1
    
    return dfs('ICN', 0)