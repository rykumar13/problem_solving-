def pair_with_targetsum(arr, target_sum):
    p1 = 0
    p2 = len(arr) - 1

    current_sum = arr[p1] + arr[p2]

    if current_sum == target_sum:
        return [p1, p2]

    while current_sum != target_sum:

        if current_sum > target_sum:
            p2 -= 1

        if current_sum < target_sum:
            p1 += 1

        current_sum = arr[p1] + arr[p2]

    return [p1, p2]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
