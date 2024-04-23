import numpy as np
import time

def standard_multiply(X, Y):
    n = len(X)
    Z = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i][j] += X[i][k] * Y[k][j]
    return Z

def split(matrix):
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen(X, Y):
    if len(X) == 1:
        return X * Y
    A, B, C, D = split(X)
    E, F, G, H = split(Y)
    P1 = strassen(A, F - H)
    P2 = strassen(A + B, H)
    P3 = strassen(C + D, E)
    P4 = strassen(D, G - E)
    P5 = strassen(A + D, E + H)
    P6 = strassen(B - D, G + H)
    P7 = strassen(A - C, E + F)
    Z11 = P5 + P4 - P2 + P6
    Z12 = P1 + P2
    Z21 = P3 + P4
    Z22 = P1 + P5 - P3 - P7
    Z_top = np.hstack((Z11, Z12))
    Z_bottom = np.hstack((Z21, Z22))
    Z = np.vstack((Z_top, Z_bottom))
    return Z

def read_input():
    n = int(input())
    X = np.array([list(map(int, input().split())) for _ in range(n)])
    Y = np.array([list(map(int, input().split())) for _ in range(n)])
    return X, Y

def compare_methods(X, Y):
    start = time.time()
    standard_multiply(X, Y)
    standard_time = time.time() - start

    start = time.time()
    strassen(X, Y)
    strassen_time = time.time() - start

    return standard_time, strassen_time

def main():
    X, Y = read_input()
    standard_time, strassen_time = compare_methods(X, Y)
    print(f"Standard method time: {standard_time:.4f} seconds")
    print(f"Strassen's method time: {strassen_time:.4f} seconds")

main()

