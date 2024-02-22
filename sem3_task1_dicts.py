"""
На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
Определите, какие вещи влезут в рюкзак backpack, передав его максимальную грузоподъёмность.
Предметы не должны дублироваться.
Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.

Пример
На входе:
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

На выходе, например, один из допустимых вариантов может быть таким:
{'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}
"""


items = {
    "ключи": '1.0',
    "кошелек": 0.0,
    "телефон": 0.0,
    "зажигалка": 0
}
max_weight = 1.0

backpack = {}
for key, value in items.items():
    items[key] = float(value)

print(items)

sorted_items = dict(sorted(items.items(), key=lambda item: item[1]))

current_weight = 0

for item, weight in sorted_items.items():
    if current_weight + weight <= max_weight:
        backpack[item] = weight
        current_weight += weight
        # backpack.values() += current_weight


print(backpack)
print(backpack.items())
print(type(backpack.items()))