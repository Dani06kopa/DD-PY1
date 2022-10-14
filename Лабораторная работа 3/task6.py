list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

min_ = list_numbers[-1]
max_ = max(list_numbers)
index_min = list_numbers.index(min_)
index_max = list_numbers.index(max_)
list_numbers[index_min] = max_
list_numbers[index_max] = min_
print(list_numbers)
