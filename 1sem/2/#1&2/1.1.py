def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    L[n1] = float('inf')  # Сигнальное значение для L
    R[n2] = float('inf')  # Сигнальное значение для R
    i = 0
    j = 0
    for k in range(left, right + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + (right - 1)) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def main():
    with open('resources/input.txt', 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))
    mergeSort(arr, 0, n-1)
    with open('resources/output.txt', 'w') as file:
        file.write(' '.join(map(str, arr)))

main()

