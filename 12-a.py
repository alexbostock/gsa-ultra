# Please write your code inside the function stub below.

def sets_of_n(l, n):
    if n == 0:
        return [[]]
    #elif n < len(l):
    elif len(l) == 0:
        return []

    a = sets_of_n(l[1:], n)
    b = sets_of_n(l[1:], n - 1)
    for x in b:
        x.append(l[0])
        a.append(x)

    return a

def combined_range(l):
    mini, maxi = l[0]

    for x in l:
        a, b = x
        mini = min(a, mini)
        maxi = max(b, maxi)

    return mini, maxi

def solution(n, x, r):
    # ranges_covered[i] should be a tuple (a, b) such that, if explosive[i] is
    # detonated, all explosives in the range x = a to b (inclusive) will be
    # detonated.
    ranges_covered = []

    overall_min = x[0]
    overall_max = x[0]

    for i in range(n):
        ranges_covered.append((x[i] - r[i], x[i] + r[i]))

        flag = True
        while flag:
            flag = False
            minimum, maximum = ranges_covered[i]
            for j in range(n):
                if x[j] < minimum:
                    minimum = x[j]
                    flag = True
                elif x[j] > maximum:
                    maximum = x[j]
                    flag = True
            ranges_covered[i] = (minimum, maximum)

            if minimum < overall_min:
                overall_min = minimum
            if maximum > overall_max:
                overall_max = maximum

    for i in range(n):
        combs = sets_of_n(ranges_covered, i + 1)
        for comb in combs:
            min, max = combined_range(comb)
            if min == overall_min and max == overall_max:
                return i + 1

print(solution(4, [2,6,7,10], [1,3,2,5]))
print(solution(10, [9,2,21,4,11,50,29,3,5,20], [1,1,9,2,1,10,3,3,2,5]))
