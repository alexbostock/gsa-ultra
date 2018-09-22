# Please write your code inside the function stub below.

def solution(s):
    counts = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
    }

    for letter in s:
        counts[letter] += 1

    pieces = []

    for i in range(4):
        pieces.append({})
        for l in counts.keys():
            pieces[i][l] = 0

    for l in counts.keys():
        c = counts[l]
        r = c % 4

        for i in range(4):
            pieces[i][l] += c // 4

        if (c // 4) % 2 == 0:
            for i in range(r):
                pieces[i][l] += 1
        else:
            for i in range(4 - r, r):
                pieces[i][l] += 1

    score = 0

    for piece in pieces:
        for l in piece.keys():
            while piece[l] > 1:
                piece[l] -= 2
                score += 2

        for l in piece.keys():
            if piece[l] == 1:
                score += 1
                break

    return score

print(solution('abccaa'))
