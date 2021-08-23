def length_of_longest_substring(word, k):
    window_start = 0
    char_count = {}
    max_repeat_letter_count = 0
    max_length = 0

    for window_end in range(len(word)):

        # traverse word one character at a time and insert it into char_count dict
        if word[window_end] not in char_count:
            char_count[word[window_end]] = 0
        char_count[word[window_end]] += 1

        # keep track of character with the greatest count so far
        max_repeat_letter_count = max(max_repeat_letter_count, char_count[word[window_end]])

        # Current window size is from window_start to window_end, overall we have a letter which is
        # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
        # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
        # if the remaining letters are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' letters
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            char_count[word[window_start]] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))


main()
