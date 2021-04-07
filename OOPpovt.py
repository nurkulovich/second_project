# ООП - парадигма, в котором чвсти программы представляются ввиде объектов

# Классы - описание объекта(спецификация)

class MyClass(object):
    attr1 = 'value'

    def method1(self):
        print('Hi!')

    @classmethod
    def method2(cls):
        print('Hello!')

    @staticmethod
    def method3():
        print(' Ciao!')
obj1 = MyClass()
obj1.a = 1
# print(obj1.__dict__)

# Типы методов
# 1.Методы экземпляра класса inctance methods
# 2.Методы класса classmethod
# 3.статическик методы static methods

# Абстракция данных - выделение значимой информации об объекте и игнорирование неважной информация
# Абстрактные методы - метод, реализациЯ которого не описана(отсуствует)
# Абстрактные классы - базовые классы в которых не указана конкретная реализациЯ методов
# или которые имеют хоть один абстрактный метод
import abc
class A(abc.ABC):
    @abc.abstractmethod
    def method1(self):
        pass

class B(A):
    def method1(self):
        print('method 1')

class A: #без использования abc
    def method1(self):
        raise NotImplementedError('Need to override method!')

class B(A):
    def method1(self):
        print('method 1')




# Наследование - процесс, при котором дочерние классы(производные) перенимают атрибуы и свойства родителей(базовых классов)
# Множественное наследование - процесс, когда дочерний класс имеет более одного родительского класса
# class A:
#     attr1 = 'value'

#     def method1(self):
#         print(self.attr1)

# class B(A):
#     pass

# b = B()
# b.method1()
# b.attr1

class A:
    def method1(self):
        print('A')

class B:
    def method1(self):
        print('B')

class C(B, A):
    def method1(self):
        super().method1()
        print('Add to logic')


# c = C()
# c.method1()
# print(c.mro())
# MRO (Method Resolution Order)[C, B, A, object]

# Инкапсуляция - набор инструментов для сокрытия внутренней реализации объектов
# Модификаторы доступа:
# 1.публичные public
#     attr1
#     method()

# 2.защищенные protected
#     _attr1
#     _method()

# 3.приватные private
#     __attr1
#     __method()

# getter - получить значение
# setter - устанавливать значение

class Car:
    _speed = 0

    def accelerate(self, new_speed):
        ...

    def decelerate(self, new_speed):
        ...

    def get_speed(self):
        return self._speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        ...

car = Car()
car.speed
car.speed = 100

# Полиморфизм
# Возможность какой-то функции обрабатывать данные разных типов при наличии у них общего интерфейса
# Магические методы, дандер методы - методы, которые отвечают за работу объектов со встроенными операторами 
# и функциями
class MyInt(int):
    def __len__(self):
        return len(str(abs(self)))

a = MyInt(3456776543)
print(len(a))

# конструктор
# деструктор

# разгица между __init__ и __new__


# __add__, __sub__...
# __eq__, __ne__...
# __len__, __contains__, __getitem__...
# __getattribute__, __setattr__, __delattr__...

# Ассоциация- когда объекты одного класса являются атрибутами другого класса

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user = User('user1', 'pass1')

class Order:
    def __init__(self, user, **details):
        self.user = user
        for k,v in details.items():
            setattr(self, k, v)

order = Order(user, total_price = 2000, products=[1,2,3])
print(order.products)

# Композиция
# Агрегация



















