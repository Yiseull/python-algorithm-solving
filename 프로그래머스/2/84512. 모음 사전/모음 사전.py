answer = 0
cnt = -1


def make_dict(word, s) -> str:
    global cnt
    cnt += 1
    
    if word == s:
        global answer
        answer = cnt
        return
    
    if len(s) == 5:
        return
    
    for i in ['A', 'E', 'I', 'O', 'U']:
        make_dict(word, s + i)

        
def solution(word) -> int:
    global answer, cnt
    make_dict(word, '')
    return answer