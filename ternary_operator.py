my_match = int(input('2 + 2 = '))
if 2 + 2 == my_match:
    print('Верно!')
else:
    print('Вы уверены?')

# тернарный оператор
my_match = int(input('2 + 2 = '))
print('Верно!' if 2 + 2 == my_match else 'Вы уверены?')