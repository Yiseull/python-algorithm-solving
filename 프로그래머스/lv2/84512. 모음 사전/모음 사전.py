answer = 0
count = 0


def find_dict(target, word):
    global count
    
    if target == word:
        global answer
        answer = count
        return
    
    if len(word) == 5:
        return
    
    for vowel in ['A', 'E', 'I', 'O', 'U']:
        count += 1
        find_dict(target, word + vowel)
        
        
def solution(word):
    find_dict(word, '')
    return answer