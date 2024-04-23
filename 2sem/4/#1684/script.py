@profile
def main():
    with open("resources/input.txt", "r") as file:
        original_word = file.readline().strip()
        last_word = file.readline().strip()

    prefixes = {original_word[:i] for i in range(1, len(original_word) + 1)}

    n = len(last_word)
    dp = [False] * (n + 1)
    dp[0] = True
    parts = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and last_word[j:i] in prefixes:
                dp[i] = True
                parts[i].append(j)

    with open("resources/output.txt", "w") as file:
        if dp[n]:
            result = []
            current = n
            while current > 0:
                next_part = min(parts[current], key=lambda x: current - x)
                result.append(last_word[next_part:current])
                current = next_part
            result.reverse()
            file.write("No\n")
            file.write(" ".join(result) + "\n")
        else:
            file.write("Yes\n")

main()
