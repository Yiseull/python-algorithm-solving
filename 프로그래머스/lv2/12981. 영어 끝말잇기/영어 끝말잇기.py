def solution(n, words):
    word_set = set()

    for i, word in enumerate(words):
        if (i > 0 and words[i - 1][-1] != word[0]) or word in word_set or len(word) == 1:
            return [i % n + 1, i // n + 1]

        word_set.add(word)

    return [0, 0]