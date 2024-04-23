def matrix_multiply_simple(X, Y):
    n = len(X)
    Z = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i][j] += X[i][k] * Y[k][j]
    return Z

def read_matrices_from_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        X = []
        Y = []
        for _ in range(n):
            X.append(list(map(int, file.readline().strip().split())))
        for _ in range(n):
            Y.append(list(map(int, file.readline().strip().split())))
    return X, Y

def main():
    filename = "resources/input.txt"
    X, Y = read_matrices_from_file(filename)

    result = matrix_multiply_simple(X, Y)

    print("Результат умножения матриц:")
    for row in result:
        print(' '.join(map(str, row)))

main()
