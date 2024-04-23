def calculate(s):
    if s.isdigit():
        return [int(s)]

    results = []
    for i in range(1, len(s), 2):
        left = calculate(s[:i])
        right = calculate(s[i + 1:])
        op = s[i]

        for l in left:
            for r in right:
                if op == '+':
                    results.append(l + r)
                elif op == '-':
                    results.append(l - r)
                elif op == '*':
                    results.append(l * r)

    return results


@profile
def solve_expression():
    with open('resources/input.txt', 'r') as file:
        s = file.readline().strip()

    max_result = max(calculate(s))

    with open('resources/output.txt', 'w') as file:
        file.write(str(max_result))


solve_expression()