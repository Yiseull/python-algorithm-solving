from collections import defaultdict

def solution(my_string):
    my_dict = defaultdict(int)
    
    for s in my_string:
        my_dict[s] += 1
        
    return ''.join(my_dict.keys())