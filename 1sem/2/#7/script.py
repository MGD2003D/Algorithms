import random


def max_subarray_sum(arr):
    max_ending_here = max_so_far = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            s = i
        else:
            max_ending_here += arr[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i

    return max_so_far, start, end

@profile
def main(input_file_path, output_file_path):
    n = 20000
    arr = [random.randint(-10 ** 9, 10 ** 9) for _ in range(n)]

    with open(input_file_path, 'w') as file:
        file.write(f"{n}\n")
        file.write(' '.join(map(str, arr)))

    with open(input_file_path, 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))

    max_sum, start, end = max_subarray_sum(arr)

    with open(output_file_path, 'w') as file:
        file.write(f"Maximum subarray length: {max_sum}, starting from index {start + 1} to {end + 1}")



input_file_path = 'resources/input.txt'
output_file_path = 'resources/output.txt'

main(input_file_path, output_file_path)
