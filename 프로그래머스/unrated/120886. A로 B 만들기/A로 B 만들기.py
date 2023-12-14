from collections import Counter

def solution(before, after) -> int:
    return 1 if Counter(before) == Counter(after) else 0