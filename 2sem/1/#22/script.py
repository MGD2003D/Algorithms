def check_compatibility(x, y, n):
    b = [0] * 5

    for i in range(n - 1):
        b[1] = 0 if (x & (1 << i)) == 0 else 1
        b[2] = 0 if (x & (1 << i + 1)) == 0 else 1
        b[3] = 0 if (y & (1 << i)) == 0 else 1
        b[4] = 0 if (y & (1 << i + 1)) == 0 else 1
        if b[1] == b[2] and b[2] == b[3] and b[3] == b[4]:
            return False
    return True

@profile
def count_unique_patterns(n, m):
    res = 0
    len_ = 1 << n
    patterns = [[0 for _ in range(len_)] for _ in range(m)]
    compatibility = [[0 for _ in range(len_)] for _ in range(len_)]

    for i in range(len_):
        for j in range(len_):
            compatibility[i][j] = 1 if check_compatibility(i, j, n) else 0

    for i in range(len_):
        patterns[0][i] = 1

    for x in range(1, m):
        for i in range(len_):
            for j in range(len_):
                patterns[x][i] += patterns[x - 1][j] * compatibility[j][i]

    for i in range(len_):
        res += patterns[m - 1][i]
    return res

with open('resources/input.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    if n > m:
        n, m = m, n

result = count_unique_patterns(n, m)

with open('resources/output.txt', 'w') as file:
    file.write(str(result))
