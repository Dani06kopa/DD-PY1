import random

def random_list(n):
  array = []
  num = random.randint(-10, 10) #обе границы включены
  for i in range(n):
    while num in array:
      num = random.randint(-10, 10)
    array.append(num)
  return array

n = 15

print("Список случайных чисел: ", random_list(n))
print("Количество уникальных значений: ", len(set(random_list(n))))
