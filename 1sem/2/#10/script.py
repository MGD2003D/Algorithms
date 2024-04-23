@profile
def merge_sort(A, left=0, right=None):
    if right is None:
        right = len(A) - 1
    if left < right:
        q = (left + right) // 2
        merge_sort(A, left, q)
        merge_sort(A, q + 1, right)
        if A[q] > A[q + 1]:
            merge(A, left, q, right)

def merge(A, left, q, right):
    L = A[left:q+1]
    R = A[q+1:right+1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

A = [5, 2, 4, 7, 1, 3, 2, 6]
merge_sort(A)
print(A)
