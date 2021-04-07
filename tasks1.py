# """
# 1) Объявите 3 переменных, запишите в них строку, список и словарь. Затем запишите их в список, и пройдитесь по нему циклом чтобы распечатать длину сразу каждого из объектов.
a = 'hello'
b = [1, 2, 3, 4]
c ={'a': 1, 'b': 2, 'c': 3}
x = [a, b, c]
# for i in x:
#     print(len(i))
# print([len(i) for i in x])



# 2) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать "Гав", для кошек "Мяу".
# Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice()

class Dog:
    def voice(self):
        print('Gav')

class Cat:
    def voice(self):
        print('Mow')

d = Dog()
c = Cat()
def to_pet(a):
    a.voice()

# to_pet(d)
# to_pet(c)



# 3. Создайте 2 класса: MyInt и MyString, наследуйте MyInt от int, MyString от str. У обоих
# классов переопределите метод, который отвечает за работу с оператором “+”.
# Напишите функцию add_objects(), которая принимает объект одного из 2 типов.
# При сложении объектов класса MyInt должно выдаваться сообщение “Это сложение”, а
# потом идти логика сложения 2 чисел, и выдача результата.
# При конкатенации объектов класса MyString() Должно выдаваться сообщение: “Это
# конкатенация”, а затем логика конкатенации из базового класса и выдача результата.

class MyInt(int):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print('Это сложение')
        return self.value + other

class MyString(str):
    def __init__(self, string):
        self.string = string

    def __add__(self, other):
        print('Это конкатенация.')
        return self.string + other
        
    # def __str__(self):
    #     return self.string

def add_objects(x, y):
    return f'{x} + {y} = {x+y}'

a = MyInt(5)
b = MyInt(6)
print(add_objects(a, b))
i = MyString('Hello')
j = MyString('World')
print(add_objects(i, j))


# 4) Создайте 3 класса: Person, Employee и Student, при этом Employee и Student должны наследоваться от Person. Определите во всех трёх классах метод get_info():
# -для класса Person он должен принимать и возвращать следующее: “Привет, меня зовут Иван Петров”.
# -для класса Employee он должен принимать и возвращать: “Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор”.
# -для класса Student должно приниматься и возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.
# Определите функцию get_human_info(), которая будет принимать объект одного из трёх классов, вызывать метод get_info и печатать результат.

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def get_info(self):
        return f'Привет, меня зовут {self.name} {self.last_name}'

class Employee(Person):
    def __init__(self, name, last_name, work, rang):
        super().__init__(name, last_name)
        self.work = work
        self.rang = rang

    def get_info(self):
        return f'{super().get_info()}, я работаю в компании "{self.work}" на должности "{self.rang}"'

class Student(Person):
    def __init__(self, name, last_name, univer, course):
        super().__init__(name, last_name)
        self.univer = univer
        self.course = course

    def get_info(self):
        return f'{super().get_info()}, я учусь в {self.univer.upper()} на {self.course} курсе'

def get_human_info(human):
    return human.get_info()

pers1 = Person('Ivan', 'Petrov')
emp1 = Employee('Ivan','Petrov', "Рога и Копыта", "директор")
st1 = Student('Ivan', 'Petrov', 'КГТУ', 3)

print(get_human_info(pers1))
print(get_human_info(emp1))
# print(get_human_info(st1))





# 5) Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.

# Затем наследуйте от Shape три класса: Triangle, Square и Circle.
# -треугольник создаётся с заданными основанием и высотой
# -квадрат создаётся с заданной длиной стороны
# -круг создаётся с заданным радиусом
# Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.

# Затем создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area()

# Подсказка: для создания абстрактных классов воспользуйтесь модулем abc
# """
# # писать код здесь

import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def get_area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return f'площадь треугольника с основанием {self.base} и высотой {self.height} равна: {self.base * self.height * 0.5}'

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return f'Площадь квадрата с стороной {self.side} равна: {self.side ** 2}'

class Circle(Shape):
    P = 3.1415

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return f'Площадь круга с радиусом {self.radius} равна: {self.P * self.radius**2}'

# tri = Triangle(8, 4)
# print(tri.get_area())
# squ = Square(6)
# print(squ.get_area())
# circle = Circle(7)
# print(circle.get_area())