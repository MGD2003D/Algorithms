def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


@profile
def main(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))
        k = int(file.readline().strip())
        targets = list(map(int, file.readline().strip().split()))

    results = [binary_search(arr, target) for target in targets]

    with open(output_file_path, 'w') as file:
        file.write(' '.join(map(str, results)))


input_file_path = 'resources/input.txt'
output_file_path = 'resources/output.txt'

main(input_file_path, output_file_path)