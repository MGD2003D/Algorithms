def merge(arr, temp, left, mid, right):
    i, j, k = left, mid, left
    inversions = 0
    while i <= mid - 1 and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
            inversions += (mid - i)
        k += 1

    while i <= mid - 1:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inversions


def merge_sort(arr, temp, left, right):
    inversions = 0
    if left < right:
        mid = (left + right) // 2
        inversions += merge_sort(arr, temp, left, mid)
        inversions += merge_sort(arr, temp, mid + 1, right)
        inversions += merge(arr, temp, left, mid + 1, right)
    return inversions


def count_inversions(arr):
    n = len(arr)
    temp = [0] * n
    return merge_sort(arr, temp, 0, n - 1)


@profile
def main():
    input_file_path = 'resources/input.txt'
    output_file_path = 'resources/output.txt'

    with open(input_file_path, 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))

    inversions = count_inversions(arr)

    with open(output_file_path, 'w') as file:
        file.write(str(inversions))


main()
