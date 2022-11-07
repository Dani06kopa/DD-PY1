from random import sample
import string


def get_random_password(n = 8) -> str:
  symbols = string.ascii_uppercase + string.digits + string.ascii_lowercase
  return ''.join(sample(symbols, n))

print(get_random_password())
