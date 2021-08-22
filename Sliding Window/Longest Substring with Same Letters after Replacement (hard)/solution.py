def max_sub_array_of_size_k(k, arr):
    max_sum, current_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        current_sum += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[window_start]
            window_start += 1

    return max_sum


arr_in = [2, 1, 5, 1, 3, 2]
k_in = 3
print(max_sub_array_of_size_k(k_in, arr_in))
