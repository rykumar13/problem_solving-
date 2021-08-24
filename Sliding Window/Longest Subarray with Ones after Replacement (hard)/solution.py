def length_of_longest_substring(arr, k):
    window_start = 0
    ones_count = 0
    longest_str_so_far = 0

    for windows_end in range(len(arr)):

        # keep track of how many 1's we have encountered so far
        if arr[windows_end] == 1:
            ones_count += 1

        # since we know how many 1's we have encountered so far
        # the remaining elements have to be 0's
        # check if the number of 0's are greater than k
        while windows_end - window_start + 1 - ones_count > k:

            # before shrinking window, check if outgoing element is a 1
            # if so, update ones_count
            if arr[window_start] == 1:
                ones_count -= 1

            # we are free to shrink the window at this point
            window_start += 1

        longest_str_so_far = max(longest_str_so_far, windows_end-window_start+1)

    return longest_str_so_far


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
