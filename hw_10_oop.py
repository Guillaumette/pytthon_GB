"""hw_10_OOP.ipynb
Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.

Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и добавляют дополнительные атрибуты и методы:

Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.

Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth,
который возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к категории "Мелководная рыба".
Если максимальная глубина обитания рыбы больше 100, то она относится к категории "Глубоководная рыба".
В противном случае, рыба относится к категории "Средневодная рыба".

Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего
(Малявка, Обычный, Гигант) в зависимости от веса. Если вес объекта меньше 1, то он относится к категории "Малявка".
Если вес объекта больше 200, то он относится к категории "Гигант".
В противном случае, объект относится к категории "Обычный".

Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе переданного
типа и параметров. Класс-фабрика должен иметь метод create_animal, который принимает следующие аргументы:

animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
*args - переменное количество аргументов, представляющих параметры для конкретного типа животного.
Количество и типы аргументов могут различаться в зависимости от типа животного.

Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.

Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция вызовет ValueError с сообщением 'Недопустимый тип животного'.

На входе:

Создание экземпляров животных

animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

Вывод результатов

print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())

На выходе:

100.0

Средневодная рыба

Гигант
"""

class Animal:
  def __init__(self, name):
    self.name = name


class Bird(Animal):
  def __init__(self, wingspan):
    super().__init__()
    self.wingspan = wingspan

    def wing_length():
      return wing_length


class Fish(Animal):
  def __init__(self, max_depth):
    super().__init__()
    self.max_depth = max_depth

  def depth(max_depth):
    if max_depth < 10:
      print('Мелководная рыба')
    elif max_depth > 100:
      print('Глубоководная рыба')
    else:
      print('Средневодная рыба')


class Mammal(Animal):
  def __init__(self, weight):
    super().__init__()
    self.weight = weight

  def category(weight):
    if weight < 1:
      print('Малявка')
    elif weight > 200:
      print('Гигант')
    else:
      print('Обычный')


class AnimalFactory:
  def create_animal(animal_type, *args):

