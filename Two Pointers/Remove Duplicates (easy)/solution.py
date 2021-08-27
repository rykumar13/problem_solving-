def remove_duplicates(arr):
    count = {}

    for element in range(len(arr)):

        if arr[element] not in count:
            count[arr[element]] = 0
        count[arr[element]] += 1

    return len(count.keys())


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
