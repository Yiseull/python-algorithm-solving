from collections import deque
from math import ceil

def solution(progresses, speeds):
    answer = []
    days = []
    
    for i, progress in enumerate(progresses):
        days.append(ceil((100 - progress) / speeds[i]))    
        
    cnt, pre = 0, days[0]
    for day in days:
        if day > pre:
            answer.append(cnt)
            cnt, pre = 1, day
        else:
            cnt += 1
    answer.append(cnt)
    
    return answer