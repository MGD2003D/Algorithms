def multiply_polynomials(A, B):
    n = len(A) + len(B) - 1
    C = [0] * n
    for i in range(len(A)):
        for j in range(len(B)):
            C[i + j] += A[i] * B[j]
    return C


@profile
def read_and_multiply(input_filename, output_filename):
    with open(input_filename, 'r') as input_file:
        n = int(input_file.readline().strip())
        A = list(map(int, input_file.readline().strip().split()))
        B = list(map(int, input_file.readline().strip().split()))

    C = multiply_polynomials(A, B)

    with open(output_filename, 'w') as output_file:
        output_file.write(' '.join(map(str, C)))


input_filename = 'resources/input.txt'
output_filename = 'resources/output.txt'
read_and_multiply(input_filename, output_filename)