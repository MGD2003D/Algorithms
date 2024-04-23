@profile
def selection_sort_swap(A):
    swaps = []
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
        if min_idx != i:
            A[i], A[min_idx] = A[min_idx], A[i]
            swaps.append((i + 1, min_idx + 1))
    return swaps

with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    A = list(map(int, file.readline().split()))

swaps = selection_sort_swap(A)

with open('output.txt', 'w') as file:
    for i, swap in enumerate(swaps):
        if i > 0:
            file.write('\n')
        file.write(f'Swap elements at indices {swap[0]} and {swap[1]}.')
    if swaps:
        file.write('\n')
    file.write('No more swaps needed.')

