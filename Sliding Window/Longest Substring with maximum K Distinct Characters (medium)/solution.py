# Example 1:
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

def longest_substring_with_k_distinct(str1, k):
    window_start = 0
    char_count = {}
    longest_window_sofar = 0

    for window_end in str1:

        if window_end not in char_count:
            char_count.update({window_end: 0})
        char_count[window_end] += 1

        while len(char_count.keys()) > k:

            char_count[str1[window_start]] -= 1
            if char_count[str1[window_start]] == 0:
                del char_count[str1[window_start]]

            window_start += 1

            longest_window_sofar = max(longest_window_sofar, sum(char_count.values()))

    return longest_window_sofar

str1_in = "araaci"
k_in = 2
print(longest_substring_with_k_distinct(str1_in, k_in))
