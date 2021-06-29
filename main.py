from random import randint

# 1. Знайти найменше число в списку
lst = [1, 2, 3]
minimum = min(lst)


# print(f"task one find minimum = {minimum}")

# 2. Вивести в циклі всі парні числа до 100, крім 6, 8, 86 якщо число 90 зустрінеться в
# списку то перервати його роботу

def get_sprcific_even_numbers(lst: lst) -> lst:
    """функція виводить всі парні числа до 100 крім 6,8,86, при знаходженні числа 90 вих
    одимо"""
    for i in lst:
        if (i % 2) == 0:
            if i == 6:
                continue
            elif i == 8:
                continue
            elif i == 86:
                continue
            elif i == 90:
                break
            else:
                print(i)
                #саме тут ми і виводимо
    return 1


# print('task second print even numbers')
# get_sprcific_even_numbers(range(0,101))
# print('task second print even numbers')

# 3. Написати функцію що перевіряє чи є строка правильно записаний номер телефона (
# +380ХХ-ХХХ-ХХ-ХХ )
def is_phone_number(value) -> bool:
    value = str(value)
    NORMAL_LEN = 16
    SEPARATOR = '-'
    is_normal_length = False
    if len(value) == NORMAL_LEN:
        is_normal_length = True
    else:
        # print('length check')
        return False

    is_start_with = False
    if value.startswith('+380'):
        start_with = True
        value = value[4:]
    else:
        # print('start with check')
        return False

    is_normal_separete = False
    if value[2] == SEPARATOR and value[6] == SEPARATOR and value[9] == SEPARATOR:
        is_normal_separete = True
        value.replace(SEPARATOR, '')
    else:
        # print('separator check')
        return False

    is_number = True

    for i in value:
        if i.isalpha():
            #    print('is alpha chech')
            return False

    if is_normal_length and start_with and is_normal_separete and is_number:
        return True


# print(is_phone_number('+38063-586-34-22'))

# 4. Скільки існує комбінацій пароля 4 символів, якщо відомо що друга цифра 4, 5 або 7,
# перша не 0, третя менша 6 а четверта більша 7
def counter_conbinations() -> int:
    counter = 0
    for i in range(1, 10):
        for k in [4,5,7]:
            for j in range(0,6):
                for r in range(8,10):
                    counter++
            
    return counter


#print(counter_conbinations())

# 5. За допомогою filter залишити в списку тільки числа кранні 8

lst_random_ints = []
[lst_random_ints.append(randint(0, 100)) for x in range(10000)]

lst_filtered = list(filter(lambda x: ((x % 8) == 0), lst_random_ints))


# print(lst_filtered)

# 6. Дано список цілих чисел, порахувати скільки чисел з цього списку мають парну
# кількість цифр
def counter_even_length(lst: lst) -> int:
    counter = 0
    for i in lst:
        if (len(str(i)) % 2) == 0:
            counter += 1
    return (counter)


# print(counter_even_length(lst_random_ints))

# 8. Дано ціле число що містить тільки цифри 9 і 6, використовуючи всього одну заміну
# цифри в числі знайти максимальне число.
# Приклад: 9669 -> 9969

def get_max_strange_number(number: int) -> int:
    number = str(number)
    for i in number:
        if not (i == str(6) or (i == str(9))):
            return (0)
    return int(number.replace('6', '9', 1))


# print(get_max_strange_number(6996))

# 9.Дано ціле число n, згенерувати список довжиною n, сума елементів якого яких рівна 0.
# (Числа повинні бути унікальні) ( і не повинні бути послідовними )
def get_list(length, MAX_INT: int = 1000000, MIN_INT: int = -1000000) -> list:
    tmp_lst = []
    for i in range(length - 1):
        tmp_randint = randint(MIN_INT, MAX_INT)
        while tmp_randint in tmp_lst:
            tmp_randint = randint(MIN_INT, MAX_INT)
        tmp_lst.append(tmp_randint)
    remainder = -(sum(tmp_lst))
    while remainder in tmp_lst:
        tmp_lst[-1] = randint(MIN_INT, MAX_INT)
        remainder = -(sum(tmp_lst))
    tmp_lst.append(remainder)
    return (tmp_lst)


# 10. Дано дві строки, перевірити чи є вони анаграмою. Тобто чи з першої строки можна
# получить іншу за допомогою перестановок
def is_anagram(string1: str, string2: str) -> bool:
    tmp_lst1 = list(string1)
    tmp_lst1.sort()
    tmp_lst2 = list(string2)
    tmp_lst2.sort()
    if tmp_lst1 == tmp_lst2:
        return True
    else:
        return False


a = "Lorem ipsum dolor"
b = "Lorem ipsum dolor"

print(is_anagram(a, b))

#11.Є файл з даними учнів у форматі Прізвище;ім’я;зріст Написати функцію що зчитує дані з файлу, функцію що добавляє учня до
#файлу, функцію що перевіряє чи є валідним формат даних що вводить користувач
import os.path

import csv

filename = 'tets.csv'

file_exists = os.path.isfile(filename)

need_write = True

while need_write:


    firstname = input('введите Ваше имя: ')
    secondname = input('введите Вашу фаилию: ')
    height = input('введите Ваш рост: ')
    if firstname.isalpha() and secondname.isalpha() and height.isdigit():
        with open(filename, 'a') as csvfile_write:
            headers = ['first name', 'second name', 'height']
            writer = csv.DictWriter(csvfile_write, delimiter=',', lineterminator='\n', fieldnames=headers)
            if not file_exists:
                writer.writeheader()
            writer.writerow({'first name': firstname,  'second name': secondname, 'height': height})
    else:
        print('Вы ввели неверные данные, введите заново')
    tmp_value_for_flag = input('для продолжения записи введите "0" \n')
    if tmp_value_for_flag != "0":
        need_write = False

a = input('для отображения списка нажмите "1"')
if a == '1':
    with open(filename, 'r') as csvfile_read:
        reader = csv.DictReader(csvfile_read)
        for row in reader:
            print(row['first name'], row['second name'], row['height'])
