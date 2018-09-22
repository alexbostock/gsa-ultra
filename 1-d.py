# Please write your code inside the function stub below.

# Identify clusters, which could be arranged in any permutation

# Product of number of permutations for each cluster

def update_clusters(pair, clusters):
    x, y = pair

    inserted_into = []

    for cluster in clusters:
        if x in cluster or y in cluster:
            cluster.add(x)
            cluster.add(y)
            inserted_into.append(cluster)

    if inserted_into == []:
        cluster = set()
        cluster.add(x)
        cluster.add(y)
        clusters.append(cluster)
    else:
        # Merge sets where required
        union = set()
        for cluster in inserted_into:
            union = union | cluster

        for cluster in clusters:
            if cluster in inserted_into:
                clusters.remove(cluster)

        clusters.append(union)

def mod_fact(n):
    ans = n
    for i in range(n):
        if i > 0:
            ans *= i
            ans = ans % 1000000007

    return ans

def solution(n, c):
    clusters = []

    for pair in c:
        update_clusters(pair, clusters)
    
    ans = 1

    for cluster in clusters:
        ans *= mod_fact(len(cluster))
        ans = ans % 1000000007

    return ans
