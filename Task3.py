from random import randint

num = 15

def get_unique_list_numbers() -> list[int]:
    list_password = []
    while len(list_password)<num:
        list_password.append(randint(-10,10))
        list_password = list(set(list_password))
    return list_password


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
