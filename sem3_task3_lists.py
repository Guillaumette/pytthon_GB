"""
Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

lst = [2, 1, 3, 6, 5, 4, 7]
# lst = [1, 2, 3, 2, 4, 5, 4]
sorted_lst = sorted(lst)

new_lst = []
# Проверим список на уникальность
setlst = set(lst)
if len(lst) != len(setlst): # есть дубликаты
    for i in sorted_lst:
        if sorted_lst.count(i) > 1:
            new_lst.append(i)

print(list(set(sorted(new_lst))))