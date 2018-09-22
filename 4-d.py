# Please write your code inside the function stub below.

def find_prods(fibonarcos, l, r, x, fibs, already_seen):
    if x > r or len(fibs) == 0 or (x, fibs[0]) in already_seen:
        return

    already_seen.add((x, fibs[0]))

    if l <= x and x <= r:
        fibonarcos[x - l] = True

    find_prods(fibonarcos, l, r, x, fibs[1:], already_seen)

    i = 0
    while x * fibs[0] ** i <= r:
        find_prods(fibonarcos, l, r, x * fibs[0] ** i, fibs[1:], already_seen)
        i += 1
        if fibs[0] == 1 or x == 0:
            break

def solution(l, r):
    fibs = []

    x = y = 1
    while y <= r:
        x, y = y, x+y
        fibs.append(x)

    fibonarcos_in_range = []
    for i in range(r - l + 1):
        fibonarcos_in_range.append(False)

    find_prods(fibonarcos_in_range, l, r, 1, fibs, set())

    ans = 0
    for x in fibonarcos_in_range:
        if not x:
            ans += 1

    return ans

print(solution(3, 9))
