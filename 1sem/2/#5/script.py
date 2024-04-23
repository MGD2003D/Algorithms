def find_majority_element(arr):
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    if arr.count(candidate) > len(arr) // 2:
        return 1
    else:
        return 0


@profile
def main(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))

    result = find_majority_element(arr)

    with open(output_file_path, 'w') as file:
        file.write(str(result))


input_file_path = 'resources/input.txt'
output_file_path = 'resources/output.txt'

main(input_file_path, output_file_path)