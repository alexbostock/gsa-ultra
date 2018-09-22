# Please write your code inside the function stub below.

# Store list of unique values and frequencies as areas

# 12915

def insert_small(l, v, k):
    if len(l) >= k and v > l[k-1]:
        return
    elif len(l) == 0 or v >= l[-1]:
        l.append(v)
        return

    i = len(l) - 1
    while i > 0 and l[i] > v:
        i -= 1
    
    l.insert(i, v)

def insert_big(l, v, k):
    if len(l) >= k and v < l[k-1]:
        return
    elif len(l) == 0 or v <= l[-1]:
        l.append(v)
        return

    i = len(l) - 1
    while i > 0 and l[i] < v:
        i -= 1
    
    l.insert(i, v)

def solution(n, m, r, c, k):
    rev = k > (len(r) - 1) * (len(c) - 1) / 2

    heights = []
    widths = []
    
    for i in range(len(r) - 1):
        heights.append(r[i+1] - r[i])
    
    for i in range(len(c) - 1):
        widths.append(c[i+1] - c[i])
    
    if rev:
        k = len(heights) * len(widths) - k + 1
    
    heights.sort(reverse=rev)
    widths.sort(reverse=rev)
    
    heights = heights[:k]
    widths = widths[:k]
    
    areas = []
    
    for h in heights:
        if len(areas) > k:
            areas = areas[:k]
        for w in widths:
            a = h * w
            if rev:
                if len(areas) >= k and a <= areas[k-1]:
                    break
                
                insert_big(areas, a, k)
            else:
                if len(areas) >= k and a >= areas[k-1]:
                    break
                
                insert_small(areas, a, k)

        if rev:
            if len(areas) >= k and h <= areas[k-1]:
                break
        else:
            if len(areas) >= k and h >= areas[k-1]:
                break

    return areas[k-1]

f = open('/Users/bossie/Downloads/downloadable_input-7.txt', 'r')
x = f.read().split('\n')

n = x[0].split(' ')[0]
m = x[0].split(' ')[1]
r = x[1].split(' ')
c = x[2].split(' ')
k = x[3]

n = int(n)
m = int(m)
for i in range(len(r)):
    r[i] = int(r[i])

for i in range(len(c)):
    c[i] = int(c[i])

k = int(k)

print(solution(n, m, r, c, k))
