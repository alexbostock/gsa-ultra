# Please write your code inside the function stub below.

def valid_next_moves(n, a, b, x, y, alice_next):
    ans = []
    
    for i in range(1, 4):
        j = n - i
        if j < 0:
            continue

        if alice_next:
            if not (j % a == 0 or j % b == 0):
                ans.append(i)
        else:
            if not (j % x == 0 or j % y == 0):
                ans.append(i)
    
    return ans

def winner(n, a, b, x, y):
    alice_allowed = []
    bob_allowed = []

    for i in range(n):
        if i == 0:
            alice_allowed.append(True)
            bob_allowed.append(True)
        else:
            alice_allowed.append(i % a != 0 and i % b != 0)
            bob_allowed.append(i % x != 0 and i % y != 0)

    alice_loses = []
    bob_loses = []

    for i in range(n):
        if i == 0:
            alice_loses.append(True)
            bob_loses.append(True)
        else:
            a = True
            b = True

            for j in range(1, 4):
                if i - j < 0:
                    continue

                if alice_allowed[i - j]:
                    a = False
                if bob_allowed[i - j]:
                    b = False

            alice_loses.append(a)
            bob_loses.append(b)

    attractiveness_a = []
    attractiveness_b = []

    for i in range(n):
        if alice_loses[i]:
            attractiveness_b.append(100)

    for i in range(n):
        if bob_loses[i]:
            attractiveness_b.append(100)

def solution(t_n, t_a, t_b, t_x, t_y):
    total = 0
    for i in range(len(t_n)):
        if winner(t_n[i], t_a[i], t_b[i], t_x[i], t_y[i]):
            total += 1

    return total + 123

print(solution([7],[5],[6],[4],[3]))
