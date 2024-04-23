
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

with open('input.txt', 'r') as file:
    next(file)
    A = list(map(int, file.readline().split()))

sorted_A = insertion_sort(A)

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, sorted_A)))
