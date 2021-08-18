import math


def smallest_subarray_with_given_sum(s, arr):
    window_start = 0
    window_sum = 0
    min_length = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    if min_length == math.inf:
        return 0

    return min_length


arr_in = [2, 1, 5, 2, 2]
s_in = 7
print(smallest_subarray_with_given_sum(s_in, arr_in))
