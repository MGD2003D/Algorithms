
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def read_array_from_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))
    return arr


def write_array_to_file(filename, arr):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, arr)))

input_filename = 'resources/input.txt'
output_filename = 'resources/output.txt'

arr = read_array_from_file(input_filename)

n = len(arr)
quicksort(arr, 0, n-1)

write_array_to_file(output_filename, arr)

