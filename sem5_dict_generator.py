"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.

Сумма рассчитывается как ставка умноженная на процент премии.

Не забудьте распечатать в конце результат.

Пример использования.
На входе:
names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

На выходе:
{'Alice': 500.0, 'Bob': 300.0, 'Charlie': 1050.0}
"""

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]
#
# bonus = [float(b.strip("%")) for b in bonus]  # Преобразуем проценты в числа
# result = {name: sal * b / 100 for name, sal, b in zip(names, salary, bonus)}
# print(result)

# result = {}
# for name, sal, b in zip(names, salary, bonus):
#     result[name] = sal * float(b.strip("%")) / 100
#
#
# print(result)

result = {names[i]: salary[i] * float(bonus[i].strip('%')) / 100 for i in range(len(names))}
print(result)
