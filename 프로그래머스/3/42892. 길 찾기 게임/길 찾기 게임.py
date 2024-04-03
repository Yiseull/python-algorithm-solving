import sys
sys.setrecursionlimit(10000)


def solution(nodeinfo: list) -> list:
    answer = [[], []]
    
    nodeinfo = sorted([nodeinfo[i] + [i + 1] for i in range(len(nodeinfo))])
    
    def order(graph: list) -> None:
        if graph == []:
            return
        
        root = 0
        for i in range(1, len(graph)):
            if graph[root][1] < graph[i][1]:
                root = i
            
        answer[0].append(graph[root][2])
        order(graph[:root])
        order(graph[root + 1:])
        answer[1].append(graph[root][2])
        
    order(nodeinfo)
    
    return answer