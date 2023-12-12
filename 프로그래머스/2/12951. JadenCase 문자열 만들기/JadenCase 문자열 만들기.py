def solution(s):
    s = list(s)
    for i, char in enumerate(s):
        if i == 0:
            s[i] = char.upper()
        elif s[i - 1] == ' ' and char.isalpha:
            s[i] = char.upper()
        else:
            s[i] = s[i].lower()
    
    return ''.join(s)