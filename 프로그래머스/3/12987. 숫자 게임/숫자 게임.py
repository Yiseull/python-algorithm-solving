from heapq import *


def solution(A, B):
    B.sort(reverse=True)
    answer = -1
    i = 0
    for a in sorted(A, reverse=True):
        if a < B[i]:
            i += 1
    
    return i