def to_hex(num):
    hex_digits = "0123456789abcdef"
    hex_str = ""
    while num > 0:
        hex_str = hex_digits[num % 16] + hex_str
        num //= 16
    return hex_str

hex_string = to_hex(0)
print('Шестнадцатеричное представление числа:', hex_string)
print('Проверка результата:', hex(0))

hex_string = to_hex(16)
print('Шестнадцатеричное представление числа:', hex_string)
print('Проверка результата:', hex(16))

hex_string = to_hex(255)
print('Шестнадцатеричное представление числа:', hex_string)
print('Проверка результата:', hex(255))

hex_string = to_hex(4096)
print('Шестнадцатеричное представление числа:', hex_string)
print('Проверка результата:', hex(4096))

hex_string = to_hex(65535)
print('Шестнадцатеричное представление числа:', hex_string)
print('Проверка результата:', hex(65535))

hex_string = to_hex(123456)
print('Шестнадцатеричное представление числа:', hex_string)
print('Проверка результата:', hex(123456))
