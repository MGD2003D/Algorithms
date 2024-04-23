@profile
def binary_sum(A, B):
    n = len(A)
    C = [0] * (n + 1)
    carry = 0

    for i in range(n - 1, -1, -1):
        total = A[i] + B[i] + carry
        C[i + 1] = total % 2
        carry = total // 2

    C[0] = carry

    return C


with open('input.txt', 'r') as file:
    A, B = file.readline().split()
    A = [int(bit) for bit in A]
    B = [int(bit) for bit in B]

C = binary_sum(A, B)

with open('output.txt', 'w') as file:
    file.write(''.join(map(str, C)))

