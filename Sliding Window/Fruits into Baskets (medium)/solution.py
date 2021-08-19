def fruits_into_baskets(fruits):
    window_start = 0
    count = {}
    max_fruits_so_far = 0

    for window_end in fruits:

        if window_end not in count.keys():
            count.update({window_end: 0})
        count[window_end] += 1

        while len(count.keys()) > 2:

            count[fruits[window_start]] -= 1
            if count[fruits[window_start]] == 0:
                del count[fruits[window_start]]

            window_start += 1
        max_fruits_so_far = max(max_fruits_so_far, sum(count.values()))

    return max_fruits_so_far


fruit_in_1 = ['A', 'B', 'C', 'A', 'C']
fruit_in_2 =['A', 'B', 'C', 'B', 'B', 'C']
print(fruits_into_baskets(fruit_in_1))
print(fruits_into_baskets(fruit_in_2))
