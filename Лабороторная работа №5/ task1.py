from pprint import pprint

list_of_numbers = []
for i in range(16):
  number = {}
  number["bin"] =  bin(i)
  number["dec"] =  i
  number["hex"] = hex(i)
  number["oct"] = oct(i)
  list_of_numbers.append(number)

pprint(list_of_numbers)
