
from collections import deque
from math import ceil

def solution(progresses, speeds):
    answer = []
    periods = []
    
    for i, progress in enumerate(progresses):
        periods.append(ceil((100 - progress) / speeds[i]))    
        
    cnt, pre = 0, periods[0]
    for period in periods:
        if period > pre:
            answer.append(cnt)
            cnt, pre = 1, period
        else:
            cnt += 1
    answer.append(cnt)
    
    return answer