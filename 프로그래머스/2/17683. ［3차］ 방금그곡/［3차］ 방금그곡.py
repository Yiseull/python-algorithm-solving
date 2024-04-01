def calcultate_playingtime(start: str, end: str) -> int:
    start_h, start_m = map(int, start.split(':'))
    end_h, end_m = map(int, end.split(':'))
    return (end_h * 60 + end_m) - (start_h * 60 + start_m)



def solution(m: str, musicinfos: list) -> str:
    answer = ['', 0]
    
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#', 'b')
    for musicinfo in musicinfos:
        start, end, title, sheet = musicinfo.split(',')
        sheet = sheet.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#', 'b')
        playingtime = calcultate_playingtime(start, end)
        i, len_sheet, len_m = 0, len(sheet), len(m)
        for j in range(playingtime):
            if m[i] == sheet[j % len_sheet]:
                i += 1
                if i == len_m:
                    if answer[1] < playingtime:
                        answer = [title, playingtime]
                    break
            elif m[0] == sheet[j % len_sheet]:
                i = 1
                if i == len_m:
                    if answer[1] < playingtime:
                        answer = [title, playingtime]
                    break
            else:
                i = 0
    
    return answer[0] if answer[0] != '' else '(None)'