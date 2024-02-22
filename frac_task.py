"""
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
Для проверки своего кода используйте модуль fractions.

На входе:
frac1 = "1/2"
frac2 = "1/3"

На выходе:
Сумма дробей: 5/6
Произведение дробей: 1/6
Сумма дробей: 5/6
Произведение дробей: 1/6
"""

from fractions import Fraction


def sum_and_product(frac1, frac2):
    num1, denom1 = frac1.split('/')
    num2, denom2 = frac2.split('/')
    fraction1 = Fraction(int(num1), int(denom1))
    fraction2 = Fraction(int(num2), int(denom2))
    sum_fraction = fraction1 + fraction2
    product_fraction = fraction1 * fraction2
    return sum_fraction, product_fraction


f1 = '1/2'
f2 = '1/3'

sum_res, prod_res = sum_and_product(f1, f2)

print(f'Сумма дробей: {sum_res}')
print(f'Произведение дробей: {prod_res}')
