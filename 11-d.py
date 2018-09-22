# Please write your code inside the function stub below.

# Generate square numbers up to ...

# Compare each number to the list

def almost_numbers(x):
    x = str(x)
    ans = []
    for i in range(len(x)):
        ans.append(x[:i] + x[i+1:])

    return map(int, ans)

def solution(a):
    limit = max(almost_numbers(a))

    squares = []
    i = 0
    while True:
        x = i ** 2
        i += 1
        if x > limit:
            break
        else:
            squares.append(x)

    num_almost_squares = 0

    for i in range(10, a + 1):
        for x in almost_numbers(i):
            if x in squares:
                num_almost_squares += 1

    return num_almost_squares

print(solution(1234))
