def is_heap(arr, n):
    for i in range(n // 2):
        if 2*i + 1 < n and arr[i] > arr[2*i + 1]:
            return False
        if 2*i + 2 < n and arr[i] > arr[2*i + 2]:
            return False
    return True

@profile
def main():
    with open('resources/input.txt', 'r') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))

    result = "YES" if is_heap(arr, n) else "NO"

    with open('resources/output.txt', 'w') as f:
        f.write(result)

main()
