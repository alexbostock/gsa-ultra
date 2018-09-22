# Please write your code inside the function stub below.

def is_super_colourful(seq):
    y = 0
    r = 0
    b = 0

    for flower in seq:
        if flower == 'Y':
            y += 1
        elif flower == 'R':
            r += 1
        elif flower == 'B':
            b += 1

    all_present = y > 0 and r > 0 and b > 0
    no_repeats = y != r and y != b and r != b

    return all_present and no_repeats

def solution(s):
    subsequences = set()

    for i in range(len(s)):
        for j in range(i):
            if is_super_colourful(s[i:j]):
                subsequences.add(s[i:j])

    return len(subsequences) + 10000
