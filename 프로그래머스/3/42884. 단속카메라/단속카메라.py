'''
1. 진입 시점으로 정렬한다.
2. 차량의 진입 시점을 지날 때마다 진출 지점을 우선순위 큐에 넣는다.
3. 다음 차량의 진입 시점이 이전에 저장해둔 가장 작은 진출 지점보다 크면 우선순위 큐를 비우고, 정답을 +1한다.
4. 마지막 차량을 다 확인한 후 큐가 비어있지 않으면, 정답을 +1한다.
'''
from heapq import *


def solution(routes: list) -> int:
    answer = 0
    q = []
    routes.sort()
    for route in routes:
        if q and q[0] < route[0]:
            q = []
            answer += 1
        heappush(q, route[1])
            
    if q:
        answer += 1
            
    return answer