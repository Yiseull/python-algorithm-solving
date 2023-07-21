def solution(n, words):
    word_set = set([words[0]])
    
    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0] or words[i] in word_set:
            return [i % n + 1, i // n + 1]

        word_set.add(words[i])

    return [0, 0]