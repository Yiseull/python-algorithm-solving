from collections import Counter

def solution(s):
    counter = Counter(s.lower())
    return counter['p'] == counter['y']