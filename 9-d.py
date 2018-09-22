# Please write your code inside the function stub below.

# Total length (time) of shortest route * 1000

def bfs (maze, start, targets):
    ans = {}

    x, y = start
    queue = [(x, y, 0)]

    visited_nodes = set()

    while len(targets) > 0 and len(queue) > 0:
        x, y, d = queue.pop(0)
        if (x, y) in visited_nodes:
            continue

        visited_nodes.add((x, y))

        if (x, y) in targets:
            ans[(x, y)] = d
            targets.remove((x, y))

        if maze[x][y] != 'W':
            if x > 0:
                queue.append((x-1, y, d+1))
            if y > 0:
                queue.append((x, y-1, d+1))
            if x < len(maze) - 1:
                queue.append((x+1, y, d+1))
            if y < len(maze) - 1:
                queue.append((x, y+1, d+1))

    for target in targets:
        ans[target] = len(maze) ** 2

    return ans

def solution(n, m):
    reds = []
    greens = []
    blues = []

    for i in range(n):
        for j in range(n):
            if m[i][j] == 'S':
                start = (i, j)
            elif m[i][j] == 'C':
                cheese = (i, j)
            elif m[i][j] == 'R':
                reds.append((i, j))
            elif m[i][j] == 'G':
                greens.append((i, j))
            elif m[i][j] == 'B':
                blues.append((i, j))

    keys = set(reds) | set(greens) | set(blues)

    distances_s = bfs(m, start, keys.copy())
    distances_c = bfs(m, cheese, keys)

    distances_from_start = {
        'r': [],
        'g': [],
        'b': []
    }

    distances_from_cheese = {
        'r': [],
        'g': [],
        'b': []
    }

    for red in reds:
        distances_from_start['r'].append(distances_s[red])
        distances_from_cheese['r'].append(distances_c[red])

    for green in greens:
        distances_from_start['g'].append(distances_s[green])
        distances_from_cheese['g'].append(distances_c[green])

    for blue in blues:
        distances_from_start['b'].append(distances_s[blue])
        distances_from_cheese['b'].append(distances_c[blue])

    distances_from_red = []
    distances_from_green = []

    for red in reds:
        distances = {'g': [], 'b': []}

        dis = bfs(m, red, set(greens) | set(blues))

        for green in greens:
            distances['g'].append(dis[green])

        for blue in blues:
            distances['b'].append(dis[blue])

        distances_from_red.append(distances)

    for green in greens:
        distances = {'b': []}

        dis = bfs(m, red, set(blues))

        for blue in blues:
            distances['b'].append(dis[blue])

        distances_from_green.append(distances)

    shortest = n * n

    for r in range(len(reds)):
        for g in range(len(greens)):
            for b in range(len(blues)):
                # RGB RBG GRB GBR BRG BGR
                l = distances_from_start['r'][r] + distances_from_red[r]['g'][g] + distances_from_green[g]['b'][b] + distances_from_cheese['b'][b]
                shortest = min(l, shortest)

                l = distances_from_start['r'][r] + distances_from_red[r]['b'][b] + distances_from_green[g]['b'][b] + distances_from_cheese['g'][g]
                shortest = min(l, shortest)

                l = distances_from_start['g'][g] + distances_from_red[r]['g'][g] + distances_from_red[r]['b'][b] + distances_from_cheese['b'][b]
                shortest = min(l, shortest)

                l = distances_from_start['g'][g] + distances_from_green[g]['b'][b] + distances_from_red[r]['b'][b] + distances_from_cheese['r'][r]
                shortest = min(l, shortest)

                l = distances_from_start['b'][b] + distances_from_red[r]['b'][b] + distances_from_red[r]['g'][g] + distances_from_cheese['g'][g]
                shortest = min(l, shortest)

                l = distances_from_start['b'][b] + distances_from_green[g]['b'][b] + distances_from_red[r]['g'][g] + distances_from_cheese['r'][r]
                shortest = min(l, shortest)

    return shortest * 1000

print(solution(20, [
    '..R..B.B.B.G.R..W.W.',
    'W.W.W.W.W.W.W.W.W.W.',
    '.W.W.W.W.W.W.W.W.W.W',
    '.R..................',
    '.R..G......B...B....',
    '.R...............G..',
    '.R...........B......',
    '....................',
    '....R.....S.........',
    '................W...',
    '...............W....',
    '.......G......W.....',
    '............WW......',
    '...........W........',
    '..........W....W....',
    '...........W..R.W...',
    '.......C....W.B..W..',
    '.W.W.W.W.W.W.W.G..W.',
    '..WWWRW.W.W...W....W',
    '..GGRBBBB......W....',
]))
