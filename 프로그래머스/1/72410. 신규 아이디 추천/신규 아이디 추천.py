def solution(new_id) -> str:
    # 1단계
    new_id = list(new_id.lower())
    # 2단계
    for i, c in enumerate(new_id):
        if not c.isalnum() and c not in ('-', '_', '.'):
            new_id[i] = ''
    # 3단계
    cnt = 0
    newid = ''
    for i in ''.join(new_id):
        if i == '.':
            cnt += 1
        else:
            if cnt > 0:
                newid += '.'
                cnt = 0
            newid += i
    # 4단계
    if newid and newid[0] == '.': newid = newid[1:]
    if newid and newid[-1] == '.': newid = newid[:-1]
    # 5단계
    if not newid: newid = 'a'
    # 6단계
    if len(newid) > 15: newid = newid[:15]
    if newid and newid[-1] == '.': newid = newid[:-1]
    # 7단계
    while len(newid) < 3:
        newid += newid[-1]
        
    return newid