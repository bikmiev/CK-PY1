from random import choice, sample
import string

def get_random_password(length, signs) -> str:
    if length <0:
        print("ошибка, введите положительное число")
        return ''
    password = ''.join(sample(signs, length))
    return password

signs1 = list(string.ascii_uppercase+string.ascii_lowercase+string.digits)
print(get_random_password(8, signs1))
