
def insertion_sort_and_track_positions(A):
    length = len(A)
    positions = [0] * length

    for j in range(length):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
        positions[j] = i + 2

    return positions


with open('input.txt', 'r') as file:
    next(file)
    A = list(map(int, file.readline().split()))

new_positions = insertion_sort_and_track_positions(A.copy())

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, new_positions)) + '\n')
    file.write(' '.join(map(str, sorted(A))))


