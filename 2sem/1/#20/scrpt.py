def is_almost_palindrome(s, k):
    changes_needed = 0
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            changes_needed += 1
    return changes_needed <= k


def count_almost_palindromes(n, k, s):
    count = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if is_almost_palindrome(s[i:j], k):
                count += 1
    return count


@profile
def solve(input_filename, output_filename):
    with open(input_filename, 'r') as input_file:
        n, k = map(int, input_file.readline().split())
        s = input_file.readline().strip()

    result = count_almost_palindromes(n, k, s)

    with open(output_filename, 'w') as output_file:
        output_file.write(str(result))


solve('resources/input.txt', 'resources/output.txt')
