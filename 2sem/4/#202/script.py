@profile
def main():
    with open("resources/input.txt", "r") as file:
        s = file.readline().strip()
        t = file.readline().strip()

    n, m = len(s), len(t)
    d = [m] * 256

    for i in range(m - 1):
        d[ord(t[i])] = m - i - 1

    i = m - 1
    results = []

    while i < n:
        j, k = m - 1, i
        while j >= 0 and t[j] == s[k]:
            j -= 1
            k -= 1
        if j < 0:
            results.append(str(k + 1))
        i += d[ord(s[i])] if i < n else 0

    with open("resources/output.txt", "w") as file:
        file.write(" ".join(results))



main()