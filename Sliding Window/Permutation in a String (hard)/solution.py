def find_permutation(str, pattern):
    window_start = 0
    char_count = {}

    # put each char from pattern into dict
    for char in pattern:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

    for window_end in range(len(str)):

        right_char = str[window_end]

        # if char is part of pattern, decrement the dict
        if right_char in char_count:
            char_count[right_char] -= 1

            # if sum of dict is 0, we have all the chars from the pattern in the window
            if sum(char_count.values()) == 0:
                return True

        # however if not matched, shrink window
        # increment dict if char previously decremented
        while window_end-window_start+1 > len(pattern):
            window_start += 1

            left_char = str[window_start]

            if left_char in char_count:
                char_count[left_char] += 1

    return False


def main():
    print(find_permutation("oidbcaf", "abc"))
    print(find_permutation("odicf", "dc"))
    print(find_permutation("bcdxabcdy", "bcdyabcdx"))
    print(find_permutation("aaacb", "abc"))


main()
