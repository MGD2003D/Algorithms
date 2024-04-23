@profile
def find_partition(sequence):
    total_sum = sum(sequence)
    if total_sum % 2 != 0:
        return False, []

    target = total_sum // 2
    n = len(sequence)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(target + 1):
            if j >= sequence[i - 1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-sequence[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    if not dp[n][target]:
        return False, []

    part = []
    while target > 0 and n > 0:
        if dp[n][target] and not dp[n-1][target]:
            part.append(n)
            target -= sequence[n-1]
        n -= 1

    if len(part) > 1 or not part:
        return True, [len(sequence)]
    return True, part

with open('resources/input.txt', 'r') as file:
    n = int(file.readline().strip())
    sequence = list(map(int, file.readline().strip().split()))

can_be_partitioned, partition = find_partition(sequence)

with open('resources/output.txt', 'w') as file:
    if can_be_partitioned:
        file.write(f"{len(partition)}\n")
        file.write(' '.join(map(str, partition[::-1])))
    else:
        file.write("-1\n")
