def non_repeat_substring(word):
    window_start = 0
    char_count = {}
    longest_str_so_far = 0

    for window_end in word:

        if window_end not in char_count:
            char_count.update({window_end: 0})
        char_count[window_end] += 1

        while sum(char_count.values()) > len(char_count.keys()):

            char_count[word[window_start]] -= 1
            if char_count[word[window_start]] == 0:
                del char_count[word[window_start]]

            window_start += 1

        longest_str_so_far = max(longest_str_so_far, len(char_count.keys()))

    return longest_str_so_far


example_1 = 'aabccbb'
example_2 = 'abbbb'
example_3 = 'abccde'
print(non_repeat_substring(example_1))
print(non_repeat_substring(example_2))
print(non_repeat_substring(example_3))
