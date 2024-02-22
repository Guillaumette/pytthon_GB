"""
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.

Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф)
считать двумя словами.
Цифры за слова не считаем.

Отсортируйте по убыванию значения количества повторяющихся слов.
"""
import re
from collections import Counter

text = "Python 3.9 is the latest version of Python. It's awesome!"

text = text.lower()
new_text = re.sub("[^A-Za-z]", " ", text) # убирает все символы, кроме букв
print(new_text)

word_counts = Counter(new_text.split())
most_common_words = word_counts.most_common(10)

print(most_common_words)


