def lcs_of_three(a, b, c, n, m, l):
    dp = [[[0 for _ in range(l + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            for k in range(l + 1):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 0
                elif a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    return dp[n][m][l]


def read_input(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        a = list(map(int, file.readline().strip().split()))
        m = int(file.readline().strip())
        b = list(map(int, file.readline().strip().split()))
        l = int(file.readline().strip())
        c = list(map(int, file.readline().strip().split()))
    return a, b, c, n, m, l


def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))


def main():
    a, b, c, n, m, l = read_input("resources/input.txt")
    result = lcs_of_three(a, b, c, n, m, l)
    write_output("resources/output.txt", result)


main()
