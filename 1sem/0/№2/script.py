def calc_fib(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


@profile
def main():
    with open("resources/input.txt", "r") as input_file:
        n = int(input_file.readline())

    result = calc_fib(n)

    with open("resources/output.txt", "w") as output_file:
        output_file.write(str(result))


main()
