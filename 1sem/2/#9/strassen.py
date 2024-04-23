def matrix_multiply_simple(X, Y):
    n = len(X)
    Z = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i][j] += X[i][k] * Y[k][j]
    return Z


def add_matrix(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract_matrix(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C


def split_matrix(X):
    n = len(X)
    mid = n // 2
    A = [[X[i][j] for j in range(mid)] for i in range(mid)]
    B = [[X[i][j] for j in range(mid, n)] for i in range(mid)]
    C = [[X[i][j] for j in range(mid)] for i in range(mid, n)]
    D = [[X[i][j] for j in range(mid, n)] for i in range(mid, n)]
    return A, B, C, D


def strassen(X, Y):
    n = len(X)
    if n <= 2:
        return matrix_multiply_simple(X, Y)
    A, B, C, D = split_matrix(X)
    E, F, G, H = split_matrix(Y)

    P1 = strassen(A, subtract_matrix(F, H))
    P2 = strassen(add_matrix(A, B), H)
    P3 = strassen(add_matrix(C, D), E)
    P4 = strassen(D, subtract_matrix(G, E))
    P5 = strassen(add_matrix(A, D), add_matrix(E, H))
    P6 = strassen(subtract_matrix(B, D), add_matrix(G, H))
    P7 = strassen(subtract_matrix(A, C), add_matrix(E, F))

    Z11 = add_matrix(subtract_matrix(add_matrix(P5, P4), P2), P6)
    Z12 = add_matrix(P1, P2)
    Z21 = add_matrix(P3, P4)
    Z22 = subtract_matrix(subtract_matrix(add_matrix(P1, P5), P3), P7)

    Z = [[0 for _ in range(n)] for _ in range(n)]
    nZ = len(Z11)
    for i in range(nZ):
        for j in range(nZ):
            Z[i][j] = Z11[i][j]
            Z[i][j + nZ] = Z12[i][j]
            Z[i + nZ][j] = Z21[i][j]
            Z[i + nZ][j + nZ] = Z22[i][j]
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
    result = strassen(X, Y)
    print("Результат умножения матриц:")
    for row in result:
        print(' '.join(map(str, row)))



main()
