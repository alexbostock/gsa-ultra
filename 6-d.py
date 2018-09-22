# Please write your code inside the function stub below.

# Doesn't work: need to have test_set == open_nodes, not subset

def test(n, edges, test_set):
    in_deg = []
    open_nodes = set()

    for i in range(n):
        in_deg.append(0)

    for (u, v) in edges:
        in_deg[v - 1] += 1

    for i in range(n):
        if in_deg[i] == 0:
            open_nodes.add(i + 1)

    spare_nodes = open_nodes - test_set

    while len(spare_nodes) > 0:
        for n in spare_nodes:
            open_nodes.remove(n)

            for (u, v) in edges:
                if u == n + 1:
                    in_deg[v - 1] -= 1
                    if in_deg[v - 1] == 0:
                        open_nodes.add(v)

        spare_nodes = open_nodes - test_set

    return test_set == open_nodes

def solution(t):
    ans = 0
    
    for i in range(len(t)):
        n, edges, test_set = t[i]
        
        test_set = set(test_set)
        
        if test(n, edges, test_set):
            ans += 2 ** i
            ans = ans % 1000000007
    
    return ans

print(solution([
    (5, [(1,3),(2,3),(3,4),(2,5),(5,4),(1,5)],[1,5]),
    (5, [(1,3),(2,3),(3,4),(2,5),(5,4)],[1,2,5])
]))
