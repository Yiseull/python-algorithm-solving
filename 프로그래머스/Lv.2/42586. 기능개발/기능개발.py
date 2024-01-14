from collections import deque
from math import ceil


def solution(progresses: list, speeds: list) -> list:
    answer = []
    q = []
    for i, progress in enumerate(progresses):
        deploy = ceil((100 - progress) / speeds[i])
        if q and q[0] < deploy:
            answer.append(len(q))
            q = [deploy]
        else:
            q.append(deploy)
            
    if q:
        answer.append(len(q)) 
            
    return answer