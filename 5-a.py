# Please write your code inside the function stub below.

def deepcopy(x):
    y = {}
    for k in x.keys():
        y[k] = x[k].copy()

    return y

def next_index(positions, i):
    if len(positions) == 0 or positions[-1] < i:
        return -1
    else:
        x = i-1
        while x < i:
            x = positions.pop(0)

        return x

def solution(a, b):
    letter_positions = {
        'a': [],
        'b': [],
        'c': [],
        'd': [],
        'e': [],
        'f': [],
        'g': [],
        'h': [],
        'i': [],
        'j': [],
        'k': [],
        'l': [],
        'm': [],
        'n': [],
        'o': [],
        'p': [],
        'q': [],
        'r': [],
        's': [],
        't': [],
        'u': [],
        'v': [],
        'w': [],
        'x': [],
        'y': [],
        'z': [],
    }

    for i in range(len(b)):
        letter_positions[b[i]].append(i)

    letter_positions_master = deepcopy(letter_positions)

    i = 0
    num_substrings = 1

    for letter in a:
        positions = letter_positions[letter]
        i = next_index(positions, i)

        if i == -1:
            i = 0
            num_substrings += 1
            letter_positions = deepcopy(letter_positions_master)
            positions = letter_positions[letter]
            i = next_index(positions, i)

    return num_substrings

def solution(a, b):
    letter_positions = {
        'a': [],
        'b': [],
        'c': [],
        'd': [],
        'e': [],
        'f': [],
        'g': [],
        'h': [],
        'i': [],
        'j': [],
        'k': [],
        'l': [],
        'm': [],
        'n': [],
        'o': [],
        'p': [],
        'q': [],
        'r': [],
        's': [],
        't': [],
        'u': [],
        'v': [],
        'w': [],
        'x': [],
        'y': [],
        'z': [],
    }

    for i in range(len(b)):
        letter_positions[b[i]].append(i)

    current_positions = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    i = 0
    num_substrings = 1

    for letter in a:
        positions = letter_positions[letter]
        if current_positions[letter] == len(positions) or positions[-1] < i:
            i = 0
            num_substrings += 1

            for l in current_positions.keys():
                current_positions[l] = 0

            i = positions[current_positions[letter]] + 1
            current_positions[letter] += 1
        else:
            while positions[current_positions[letter]] < i:
                current_positions[letter] += 1
            i = positions[current_positions[letter]] + 1
            current_positions[letter] += 1

    return num_substrings

print(solution('xyxy', 'xyy'))
print(solution('abcabacabcaabca', 'abc'))

x = open('/Users/bossie/Downloads/downloadable_input-6.txt', 'r').read().split(' ')

print(solution(x[0], x[1][:-1]))
