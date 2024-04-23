def quicksort3(arr, low, high):
    if low < high:
        m1, m2 = partition3(arr, low, high)
        quicksort3(arr, low, m1 - 1)
        quicksort3(arr, m2 + 1, high)

def partition3(arr, low, high):
    pivot = arr[high]
    i = low
    m1 = low
    m2 = high
    while i <= m2:
        if arr[i] < pivot:
            arr[i], arr[m1] = arr[m1], arr[i]
            m1 += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[m2] = arr[m2], arr[i]
            m2 -= 1
        else:
            i += 1
    return m1, m2

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
quicksort3(arr, 0, len(arr) - 1)
write_array_to_file(output_filename, arr)
