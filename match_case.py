color = input('Твой любимый цвет: ').lower()
match color:
    case 'красный' | 'оранжевый':
        print('Любитель яркого')
    case 'зеленый':
        print('Ты не охотник?')
    case 'синий' | 'голубой':
        print('Ха, классика!')
    case _:
        print('Тебя не понять')