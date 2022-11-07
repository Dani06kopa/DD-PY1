import random

def random_list(n, left_lim, right_lim):
  array = []
  num = random.randint(left_lim, right_lim) #первое присваивание
  for i in range(n):
    while num in array:
      num = random.randint(left_lim, right_lim)
    array.append(num)
  return array


n = 15
left, right = -10, 10
print("Список случайных чисел: ", random_list(n, left, right))
print("Количество уникальных значений: ", len(set(random_list(n, left, right))))
