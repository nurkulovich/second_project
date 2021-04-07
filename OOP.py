# Полиморфизм 
# виды методов 

# Полиморфизм  - это возможность функции обрабатывать объекты разных типов

# print() - выводит в консоль(число, строка, список и т.д)

def sum_(x, y):
    return x + y

# print(sum_(12, 23))
# print(sum_('a', 'b'))
# print(sum_([1,3], [2,3,4]))

# class A:
#     def method1(self):
#         print('Hello world')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Object of class B')
#     pass

# a = A()
# b = B()


# class C:
#     def method1(self):
#         print('Object of class C')

# c = C()

# def func(obj):
#     obj.method1()

# func(a)
# func(b)
# func(c)

class Transport:
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print('Едем по дороге')

class Plane(Transport):
    def move(self):
        print('летим по воздуху')

class Train(Transport):
    def move(self):
        print('Катим по рельсам')

def get_destination(transport, location):
    if type(transport) == Car:
        print('Дешевле, но долго')
    elif type(transport) == Plane:
        print('Быстрее, но дорого')



class A:
    def __init__(self, string):
        self.string = string

    def count(self):
        a = 0
        for i in self.string:
            if i.lower() in 'eyuioa':
                a += 1
        return f'кол=во гласных: {a}\n кол=во согласных {len(self.string) - a}'


# class B(A):
#     def __init__(self, string):
#         self.string = string

#     def count(self):
#         a = 0
#         for i in self.string:
#             if i.lower() in 'qwrtpsdfghjklzxcvbnm':
#                 a += 1
#         return f'кол=во согласных: {a}'


a = A('Hello words grearter')
print(a.count())
# b = B('')
# print(b.count())

# методы экземпляра  - instance methods
# методы класса - xlass methods
# статические метдоты - sttatic method 
# @classmethod
# @staticmethod

from abc import ABC

# Реализуйте программу по следующему описанию. Есть
# классы WhatsApp, SnapChat, Telegram. При регистрации в
# WhatsApp и SnapChat необходимо передавать свой номер
# телефона, который должен быть int. При регистрации в
# Telegram необходимо передавать номер телефона и
# username. Во всех классах есть метод send, в WhatsApp он
# принимает только text и выдает строку “I am sending a text ...”
# и вместо … должен быть сам текст сообщения. В SnapChat
# send принимает image и text, при этом image должен быть
# булевым типом данных. Если image True, то выдается
# сообщение “I am sending a text … with some image ”, если
#  False - сообщение “I am sending a text … without image”. В
# Telegram метод send принимает voice message в виде строки
# и выдает сообщение “I am sending a voice message ...”.
# Создайте объекты от этих классов и вызовите метод send у
# всех объектов.

class WhatsApp:
    def __init__(self, number):
        self.number = number

    def send(self, text: str):
        return f'I am sending a text "{text}"'


class Telegram:
    def __init__(self, number, username):
        self.number = number
        self.username = username

    def send(self, voice_message):
        return f'I am sending a voice message "{voice_message}"'

class SnapChat:
    def __init__(self, number):
        self.number = number

    def send(self, text, image):
        if image:
            return f'I am sending a text "{text}" with some image'
        return f'I am sending a text "{text}" without image'

a = WhatsApp(+996552252520)
# print(a.send('Hi'))
# b = SnapChat(+996552252520)
# print(b.send('Hello', False))
# c = Telegram(+996552252520, 'Nur')
# print(c.send('Hello World'))
        
