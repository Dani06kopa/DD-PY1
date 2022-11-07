from random import sample
import string

symbols = string.ascii_uppercase + string.digits + string.ascii_lowercase

def get_random_password(n) -> str:
    return ''.join(sample(symbols, n))


print(get_random_password(8))
