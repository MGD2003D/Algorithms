def merge(arr, start, mid, end, merge_info):
    L = arr[start:mid+1]
    R = arr[mid+1:end+1]
    i = j = 0
    k = start
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    if len(L) > 1 or len(R) > 1:
        merge_info.append((start + 1, end + 1, arr[start], arr[end]))

def merge_sort(arr, start, end, merge_info):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid, merge_info)
        merge_sort(arr, mid + 1, end, merge_info)
        merge(arr, start, mid, end, merge_info)

@profile
def main():
    with open('resources/input.txt', 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))

    merge_info = []
    merge_sort(arr, 0, n - 1, merge_info)

    with open('resources/output.txt', 'w') as file:
        for info in merge_info:
            file.write(f"{info[0]} {info[1]} {info[2]} {info[3]}\n")
        file.write(' '.join(map(str, arr)))

main()
