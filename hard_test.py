# Реалізувати трикутник паскаля ( пробіли можна пропустити ):
# input n
n = 5
 
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
 
    # first element is always 1
    C = 1
    for j in range(1, i+1):
 
        # first value in a line is always 1
        print(' ', C, sep='', end='')
 
        # using Binomial Coefficient
        C = C * (i - j) // j
    print()
    
#Є список з числами, всі числа повторюються два рази, крім одного. Потрібнознайти це число.
lst = [1, 2, 2, 3, 3, 4, 4]
print(sum(set(lst))*2 - sum(lst))

#Задача3: Біржа. Є список чисел ( цін ). Знайти коли найкраще купити (перше число), і
#продати ( друге число ). Вивести профіт (від другого числа відняти перше) який отримаєте.
#Input: [7,1,5,3,6,4]
#Output: 5
#Explanation: Купити в день 2 (price = 1) і продати в день 5 (price = 6), profit = 6-1
#= 5.
#НЕ 7-1 = 6, тому що ціна продажу повинна бути більша ціни покупки.
#Задача4: Дано список довільного розміру. Знайти елемент який в списку зустрічається
#найбільше разів.
from random import random

a = [int(random()*5) for i in range(15)]
print(a)

a_set = set(a)

most_common = None
qty_most_common = 0

for item in a_set:
    qty = a.count(item)
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = item

print(most_common)

#Задача5: Знайти чи факторіал закінчується на 0. Не використовуючи перетворення в
#строку. Вивести скільки нулів в кінці факторіала.
