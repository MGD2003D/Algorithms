def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    max_left = mid
    for i in range(mid, low-1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

price_changes = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
price_diffs = [price_changes[i] - price_changes[i-1] for i in range(1, len(price_changes))]
buy_day, sell_day, profit = find_maximum_subarray(price_diffs, 0, len(price_diffs) - 1)
print(f"To get maximum profit, you need to buy on the day {buy_day + 1}, sell on the day {sell_day + 2}, the profit will be {profit}.")
