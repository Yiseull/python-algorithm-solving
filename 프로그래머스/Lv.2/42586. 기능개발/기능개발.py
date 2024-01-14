from math import ceil


def solution(progresses: list, speeds: list) -> list:
    answer = []
    q = []
    
    for progress, speed in zip(progresses, speeds):
        deploy = ceil((100 - progress) / speed)
        if q and q[0] < deploy:
            answer.append(len(q))
            q = []
        
        q.append(deploy)
            
    if q:
        answer.append(len(q)) 
            
    return answer